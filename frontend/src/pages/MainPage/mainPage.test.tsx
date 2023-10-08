import React from 'react';
import {render, fireEvent} from '@testing-library/react';
import '@testing-library/jest-dom';
import {MainPage} from "./MainPage";
import * as applyCategoriesFunc from "../../utils/applyCategories";

afterEach(jest.clearAllMocks);

describe('Main page test', () => {
  it('should render correctly', () => {
    jest.useFakeTimers()
    jest.setSystemTime(new Date('2017-01-01'))

    const rendered = render(<MainPage/>);
    expect(rendered.asFragment()).toMatchSnapshot();

    jest.useRealTimers()
  });

  it('should render correctly when click on category', () => {
    jest.useFakeTimers()
    jest.setSystemTime(new Date('2017-01-01'))

    const rendered = render(<MainPage/>);
    const button = rendered.getByText((content, element) => {
      return element?.tagName.toLowerCase() === 'div' && element.classList.contains('categories__badge') && content === 'Одежда';
    });

    fireEvent.click(button);
    expect(rendered.asFragment()).toMatchSnapshot();

    jest.useRealTimers()
  });

  it('should call applyCategories function when click on category', () => {
    const mockApplyCategories = jest.spyOn(applyCategoriesFunc, 'applyCategories');

    const rendered = render(<MainPage/>);
    const button = rendered.getByText((content, element) => {
      return element?.tagName.toLowerCase() === 'div' && element.classList.contains('categories__badge') && content === 'Одежда';
    });

    expect(mockApplyCategories).toHaveBeenCalledTimes(1);
    fireEvent.click(button);
    expect(mockApplyCategories).toHaveBeenCalledTimes(2);
  });
});
