import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import '@testing-library/jest-dom/extend-expect';
import { MainPage } from './MainPage';
import { applyCategories, updateCategories } from '../../utils';
import { useCurrentTime, useProducts } from '../../hooks';

jest.mock('../../hooks', () => {
    const originalModule = jest.requireActual('../../hooks');

    return {
        __esModule: true,
        ...originalModule,
        useCurrentTime: jest.fn(() => '13:58:00'),
    };
});

jest.mock('../../utils', () => {
    const originalModule = jest.requireActual('../../utils');

    return {
        __esModule: true,
        ...originalModule,
        applyCategories: jest.fn(() => useProducts()),
        updateCategories: jest.fn(() => ['Одежда']),
    };
});

afterEach(jest.clearAllMocks);
describe('MainPage test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call current time function', () => {
        const rendered = render(<MainPage />);

        expect(useCurrentTime).toHaveBeenCalledTimes(1);
    });

    it('should call update categories when category click', () => {
        const rendered = render(<MainPage />);

        expect(updateCategories).toHaveBeenCalledTimes(0);
        fireEvent.click(rendered.container.getElementsByClassName('categories__badge')[0]);
        expect(updateCategories).toHaveBeenCalledTimes(1);
    });

    it('should call apply categories when category click', () => {
        const rendered = render(<MainPage />);

        expect(applyCategories).toHaveBeenCalledTimes(1);
        fireEvent.click(rendered.container.getElementsByClassName('categories__badge')[0]);
        expect(applyCategories).toHaveBeenCalledTimes(2);
    });
});
