import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import { useCurrentTime, useProducts } from '../../../hooks';
import { applyCategories, updateCategories } from '../../../utils';
import { MainPage } from '../MainPage';

jest.mock('../../../utils', () => {
    const originalModule = jest.requireActual('../../../utils');

    return {
        __esModule: true,
        ...originalModule,
        applyCategories: jest.fn(() => useProducts()),
        updateCategories: jest.fn(() => ['Одежда']),
    };
});

afterEach(jest.clearAllMocks);


describe('MainPage tests', () => {
    it('should render correctly', () => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date('2017-01-01T03:01:02'));

        const { asFragment } = render(<MainPage />);

        expect(asFragment()).toMatchSnapshot();
        jest.useRealTimers();
    });

    it('should update selected categories correctly', () => {
        const { container, getAllByText } = render(<MainPage />);

        const initialSelectedCategories = container.getElementsByClassName(
            'category selected'
        );
        expect(initialSelectedCategories.length).toBe(0);

        fireEvent.click(getAllByText('Одежда')[0]);

        const updatedSelectedCategories = container.getElementsByClassName(
            'category selected'
        );
        expect(updatedSelectedCategories.length).toBe(0);
    });

    it('should render products with selected category', () => {
        const { container, getAllByText } = render(<MainPage />);

        const initialProducts = container.getElementsByClassName('product-card');
        const initialProductsCount = initialProducts.length;

        fireEvent.click(getAllByText('Электроника')[0]);

        const updatedProducts = container.getElementsByClassName('product-card');
        const updatedProductsCount = updatedProducts.length;

        expect(updatedProductsCount).toBe(4);
    });

    it('should update and apply categories when they are clicked', () => {
        const rendered = render(<MainPage />);

        expect(applyCategories).toHaveBeenCalledTimes(1);
        expect(updateCategories).toHaveBeenCalledTimes(0);

        const categories = rendered.baseElement.getElementsByClassName('categories__badge');
        fireEvent.click(categories[0]);

        expect(updateCategories).toHaveBeenCalledTimes(1);
        expect(applyCategories).toHaveBeenCalledTimes(2);
    });


});
