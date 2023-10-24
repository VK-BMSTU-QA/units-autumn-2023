import React from 'react';
import {render, fireEvent, getAllByTestId} from '@testing-library/react';
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
        const container = render(<MainPage/>);

        const categoryElementsBefore = Array.from(document.querySelectorAll('.categories__badge'));
        const categoryElementBefore = categoryElementsBefore.find((element) => element.textContent === 'Одежда');

        expect(mockApplyCategories).toHaveBeenCalledTimes(1);
        expect(categoryElementBefore).toBeTruthy();

        if (categoryElementBefore) {
            fireEvent.click(categoryElementBefore);

            const categoryElementsAfter = Array.from(document.querySelectorAll('.categories__badge'));
            const categoryElementAfter = categoryElementsAfter.find((element) => element.textContent === 'Одежда');

            expect(mockApplyCategories).toHaveBeenCalledTimes(2);
            expect(categoryElementsAfter.length).toEqual(categoryElementsBefore.length)
        }
    });
});
