export { MainPage } from './MainPage';

import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';

import { useCurrentTime, useProducts } from '../../hooks';
import { applyCategories, updateCategories } from '../../utils';

afterEach(jest.clearAllMocks);

jest.mock('../../hooks', () => {
    const originalModule = jest.requireActual('../../hooks');

    return {
        __esModule: true,
        ...originalModule,
        useCurrentTime: jest.fn(() => '12:00:00'),
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

describe('Main page', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call function displaying current time', () => {
        render(<MainPage />);
        expect(useCurrentTime).toHaveBeenCalledTimes(1);
    });

    it('should update and apply categories when they are clicked', () => {
        const rendered = render(<MainPage />);

        expect(applyCategories).toHaveBeenCalledTimes(1);
        expect(updateCategories).toHaveBeenCalledTimes(0);

        const categories =
            rendered.baseElement.getElementsByClassName('categories__badge');
        fireEvent.click(categories[0]);

        expect(applyCategories).toHaveBeenCalledTimes(2);
        expect(updateCategories).toHaveBeenCalledTimes(1);
    });
});
