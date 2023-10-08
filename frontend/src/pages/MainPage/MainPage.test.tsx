import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';

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
        const onCategoryClick = jest.fn();
        const rendered = render(<MainPage />);

        expect(onCategoryClick).toHaveBeenCalledTimes(0);
        fireEvent.click(rendered.getByText('Одежда'));
        expect(onCategoryClick).toHaveBeenCalledTimes(1);
    });
});
