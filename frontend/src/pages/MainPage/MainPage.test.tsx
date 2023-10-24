export { MainPage } from './MainPage';

import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';

import * as useCurrentTime from '../../hooks/useCurrentTime';
import * as useProducts from '../../hooks/useProducts';
import * as applyCategories from '../../utils/applyCategories';
import * as updateCategories from '../../utils/updateCategories';
import { Product } from '../../types';
import { getPrice } from '../../utils/getPrice';

afterEach(jest.clearAllMocks);

const mockUseCurrentTime = jest.spyOn(useCurrentTime, 'useCurrentTime');
mockUseCurrentTime.mockReturnValue('12:00:00');

const mockUseProducts = jest.spyOn(useProducts, 'useProducts');

const mockApplyCategories = jest.spyOn(applyCategories, 'applyCategories');
const mockUpdateCategories = jest.spyOn(updateCategories, 'updateCategories');

const checkField = (actual: Element, classname: string, expected: string) => {
    const elems = actual.getElementsByClassName(classname);
    expect(elems).toBeInstanceOf(HTMLCollection);
    expect(elems).not.toHaveLength(0);
    expect(elems[0].textContent).toEqual(expected);
};

const checkProduct = (actual: Element, expected: Product) => {
    const text = actual.getElementsByClassName('product-card__text')[0];

    checkField(text, 'product-card__name', expected.name);
    checkField(actual, 'product-card__description', expected.description);
    checkField(
        text,
        'product-card__price',
        getPrice(expected.price, expected.priceSymbol)
    );
    checkField(text, 'product-card__category', expected.category);
};

const checkProducts = (
    actual: HTMLCollectionOf<Element>,
    expected: Product[]
) => {
    expect(actual).toHaveLength(expected.length);

    let idx = 0;
    for (const card of actual) {
        checkProduct(card, expected[idx]);
        ++idx;
    }
};

describe('Main page', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call function displaying current time', () => {
        render(<MainPage />);
        expect(mockUseCurrentTime).toHaveBeenCalledTimes(1);
    });

    it('should update and apply categories when they are clicked', () => {
        const testProducts: Product[] = [
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Latest iphone, buy it now',
                price: 999,
                priceSymbol: '$',
                category: 'Электроника',
                imgUrl: '/iphone.png',
            },
            {
                id: 2,
                name: 'Костюм гуся',
                description: 'Запускаем гуся, работяги',
                price: 1000,
                priceSymbol: '₽',
                category: 'Одежда',
            },
        ];
        mockUseProducts.mockReturnValue(testProducts);

        const rendered = render(<MainPage />);

        expect(mockApplyCategories).toHaveBeenCalledTimes(1);
        expect(mockUpdateCategories).toHaveBeenCalledTimes(0);

        checkProducts(
            rendered.baseElement.getElementsByClassName('product-card'),
            testProducts
        );

        mockUpdateCategories.mockReturnValue(['Электроника']);
        const categories =
            rendered.baseElement.getElementsByClassName('categories__badge');
        fireEvent.click(categories[0]);

        expect(mockApplyCategories).toHaveBeenCalledTimes(2);
        expect(mockUpdateCategories).toHaveBeenCalledTimes(1);

        checkProducts(
            rendered.baseElement.getElementsByClassName('product-card'),
            testProducts.filter((product) => product.category === 'Электроника')
        );
    });
});
