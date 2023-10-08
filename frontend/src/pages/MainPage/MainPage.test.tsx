import React from 'react';
import {render, fireEvent} from '@testing-library/react';
import * as currentTimeHook from "../../hooks/useCurrentTime"
import '@testing-library/jest-dom';
import {MainPage} from './MainPage';
import * as applyCategoriesUtil from "../../utils/applyCategories"

afterEach(jest.clearAllMocks);
describe('MainPage test', () => {
    it('should render correctly', () => {
        const mockCurrentTime = jest.spyOn(currentTimeHook, 'useCurrentTime');
        mockCurrentTime.mockReturnValue('14:16:00')

        const rendered = render(<MainPage/>);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call applyCategories on category click', () => {
        const mockApplyCategories = jest.spyOn(applyCategoriesUtil, 'applyCategories');
        const {getByText} = render(<MainPage/>);

        const categoryElement = getByText((content, element) => {
            return element?.tagName.toLowerCase() === 'div' && element.classList.contains('categories__badge') && content === 'Одежда';
        });

        expect(mockApplyCategories).toHaveBeenCalledTimes(1);
        fireEvent.click(categoryElement);
        expect(mockApplyCategories).toHaveBeenCalledTimes(2);
    });
});
