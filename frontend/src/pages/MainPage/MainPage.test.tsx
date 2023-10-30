import React from 'react';
import { MainPage } from './MainPage';
import { fireEvent, render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { useCurrentTime } from '../../hooks/useCurrentTime';
import { getPrice } from '../../utils';
import { Product } from '../../types';

afterEach(jest.clearAllMocks);

jest.mock('../../hooks/useCurrentTime', () => {
    return {
        __esModule: true,
        useCurrentTime: jest.fn(() => '11:11:11'),
    };
});

describe('test MainPage', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();

        expect(useCurrentTime).toHaveBeenCalledTimes(1);
    });

    it('should render correct time', () => {
        const rendered = render(<MainPage />);

        const time =
            rendered.baseElement.querySelector('[data-time]')?.textContent ??
            '';
        expect(time).toEqual('11:11:11');
    });

    it('update categories on click', () => {
        const rendered = render(<MainPage />);

        const products: Product[] = [
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
            {
                id: 3,
                name: 'Настольная лампа',
                description: 'Говорят, что ее использовали в pixar',
                price: 699,
                category: 'Для дома',
                imgUrl: '/lamp.png',
            },
            {
                id: 4,
                name: 'Принтер',
                description: 'Незаменимая вещь для студента',
                price: 7000,
                category: 'Электроника',
            },
        ];
        const renderedProducts =
            rendered.baseElement.getElementsByClassName('product-card');

        function checkProduct(p: Element, i: number) {
            const card = p.getElementsByClassName('product-card__text')[0];
            expect(
                card.getElementsByClassName('product-card__name')[0].textContent
            ).toStrictEqual(products[i].name);
            expect(
                card.getElementsByClassName('product-card__description')[0]
                    .textContent
            ).toStrictEqual(products[i].description);
            expect(
                card.getElementsByClassName('product-card__category')[0]
                    .textContent
            ).toStrictEqual(products[i].category);
            expect(
                card.getElementsByClassName('product-card__price')[0]
                    .textContent
            ).toStrictEqual(
                getPrice(products[i].price, products[i].priceSymbol)
            );
        }

        expect(renderedProducts.length).toEqual(4);
        Array.from(renderedProducts).forEach(checkProduct);

        const clothesButton =
            rendered.baseElement.getElementsByClassName('categories__badge')[0];
        fireEvent.click(clothesButton);

        expect(renderedProducts.length).toEqual(1);
        expect(checkProduct(renderedProducts[0], 1));
    });
});
