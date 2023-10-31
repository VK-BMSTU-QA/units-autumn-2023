import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from "./MainPage";
import * as applyCategoriesFunc from "../../utils/applyCategories";

beforeEach(() => {
  jest.useFakeTimers()
  jest.setSystemTime(new Date('2023-10-08T12:00:00Z'))
});

afterEach(() => {
  jest.useRealTimers()
});

afterEach(jest.clearAllMocks);

describe('Main page test', () => {
  it('should render correctly', () => {
    const rendered = render(<MainPage />);
    expect(rendered.asFragment()).toMatchSnapshot();
  });

  it('should render correctly when click on category', () => {
    const rendered = render(<MainPage />);

    const button = rendered.getByTestId("Одежда");

    fireEvent.click(button);
    expect(rendered.asFragment()).toMatchSnapshot();
  });

  it('should call applyCategories function when click on category', () => {
    const mockApplyCategories = jest.spyOn(applyCategoriesFunc, 'applyCategories');

    const rendered = render(<MainPage />);
    const button = rendered.getByTestId("Одежда");

    // проверяем количество до клика
    const cardsBeforeClick = document.getElementsByClassName("product-card")
    expect(cardsBeforeClick).toHaveLength(4);

    // сколько раз вызывался обработчик после клика
    fireEvent.click(button);
    expect(mockApplyCategories).toHaveBeenCalledTimes(2);

    // количество после клика
    const cardsAfterClick = document.getElementsByClassName("product-card")
    expect(cardsAfterClick).toHaveLength(1);

    // содержимое после клика
    const card = cardsAfterClick[0];
    expect(card.id).toStrictEqual("Костюм гуся")

    // сколько раз вызывался обработчик после повторного клика
    fireEvent.click(button);
    expect(mockApplyCategories).toHaveBeenCalledTimes(3);

    // количество карточек после повторного клика
    const cardsAfterSecondClick = document.getElementsByClassName("product-card")
    expect(cardsAfterSecondClick).toHaveLength(4);
  });
});
