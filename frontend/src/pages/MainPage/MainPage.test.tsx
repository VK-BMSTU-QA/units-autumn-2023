import React from 'react';
import {render, fireEvent} from '@testing-library/react';
import * as currentTimeHook from "../../hooks/useCurrentTime"
import '@testing-library/jest-dom';
import {MainPage} from './MainPage';
import * as applyCategoriesUtil from "../../utils/applyCategories"

afterEach(jest.clearAllMocks);
describe('MainPage test', () => {
    it('should render main', () => {
        jest.spyOn(currentTimeHook, 'useCurrentTime').mockReturnValue('23:59:59');
        expect(render(<MainPage/>).asFragment()).toMatchSnapshot();
    });

    it('should call applyCategories after click on category', () => {
        const mockApplyCategories = jest.spyOn(applyCategoriesUtil, 'applyCategories');

        const categoryElement = render(<MainPage/>).getByText((content, element) => {
            return element?.tagName.toLowerCase() === 'div' && 
                element.classList.contains('categories__badge') &&
                content === 'Для дома';
        });

        expect(mockApplyCategories).toHaveBeenCalledTimes(1);

        fireEvent.click(categoryElement);
        expect(mockApplyCategories).toHaveBeenCalledTimes(2);
    });
});
