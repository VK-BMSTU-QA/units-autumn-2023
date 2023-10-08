import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import * as applyCategoriesFunc from '../../utils/applyCategories';

afterEach(jest.clearAllMocks);
describe('Main page test', () => {
    it('should render correctly', () => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date('2020-01-01T03:00:01'));

        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
        jest.useRealTimers();
    });

    it('should call callback when category click', () => {
        const mockApplyCategories = jest.spyOn(
            applyCategoriesFunc,
            'applyCategories'
        );
        const rendered = render(<MainPage />);

        expect(mockApplyCategories).toHaveBeenCalledTimes(1);
        fireEvent.click(
            rendered
                .getAllByText('Для дома')
                .find((btn) => btn.className.includes('categories__badge')) ||
                rendered.getByText('Для дома')
        );
        expect(mockApplyCategories).toHaveBeenCalledTimes(2);
    });
});
