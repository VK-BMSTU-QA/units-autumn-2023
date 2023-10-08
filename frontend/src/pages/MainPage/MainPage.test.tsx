import '@testing-library/jest-dom';

import React from 'react';

import { fireEvent, render } from '@testing-library/react';

import { useCurrentTime } from '../../hooks';
import { applyCategories, updateCategories } from '../../utils';
import { MainPage } from './MainPage';

afterEach(jest.clearAllMocks);

jest.mock('../../hooks/', () => {
    const originalModule = jest.requireActual('../../hooks/');

    return {
        __esModule: true,
        ...originalModule,
        useCurrentTime: jest.fn(() => '12:00.00'),
    };
});

jest.mock('../../utils/', () => {
    const originalModule = jest.requireActual('../../utils/');

    return {
        __esModule: true,
        ...originalModule,
        applyCategories: jest.fn(originalModule.applyCategories),
        updateCategories: jest.fn(originalModule.updateCategories),
    };
});

describe('MainPage test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call useCurrentTime once on create', () => {
        render(<MainPage />);

        expect(useCurrentTime).toHaveBeenCalledTimes(1);
    });

    it('should update selected categories on category click', () => {
        const rendered = render(<MainPage />);

        expect(updateCategories).toHaveBeenCalledTimes(0);

        fireEvent.click(rendered.getAllByText('Одежда')[0]);

        expect(updateCategories).toHaveBeenCalledTimes(1);

        fireEvent.click(rendered.getAllByText('Одежда')[0]);

        expect(updateCategories).toHaveBeenCalledTimes(2);
    });

    it('should apply categories to products on category click', () => {
        const rendered = render(<MainPage />);

        expect(applyCategories).toHaveBeenCalledTimes(1);

        fireEvent.click(rendered.getAllByText('Электроника')[0]);

        expect(applyCategories).toHaveBeenCalledTimes(2);

        fireEvent.click(rendered.getAllByText('Электроника')[0]);

        expect(applyCategories).toHaveBeenCalledTimes(3);
    });
});
