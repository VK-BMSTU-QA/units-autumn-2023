import {render, fireEvent} from '@testing-library/react';
import '@testing-library/jest-dom';
import {MainPage} from "./MainPage";
import { useCurrentTime} from '../../hooks';
import * as applyCategoriesFunc from "../../utils/applyCategories";

afterEach(jest.clearAllMocks);

jest.mock('../../hooks/useCurrentTime', () => {
    return {
        useCurrentTime: jest.fn(() => '04:20:00'),
    };
});

describe('Main page test', () => {
  it('check render with time', () => {
    const rendered = render(<MainPage/>);
    expect(rendered.asFragment()).toMatchSnapshot();

    expect(useCurrentTime).toHaveBeenCalledTimes(1);
  });

  it('check call apply categories', () => {
    const mockApplyCategories = jest.spyOn(applyCategoriesFunc, 'applyCategories');

    const rendered = render(<MainPage/>);
    const button = rendered.baseElement.getElementsByClassName(
        'categories__badge'
    )[1]
    expect(mockApplyCategories).toHaveBeenCalledTimes(1);

    fireEvent.click(button);
    expect(mockApplyCategories).toHaveBeenCalledTimes(2);
    
  });
});