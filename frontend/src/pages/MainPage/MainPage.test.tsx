import {render, fireEvent} from '@testing-library/react';
import '@testing-library/jest-dom';
import {MainPage} from './MainPage';
import {PriceSymbol, Product, Category} from '../../types';
import {updateCategories} from "../../utils";

const products: Product[] = [
    {
        id: 1,
        name: 'MacBook',
        description: 'M2',
        price: 1400,
        priceSymbol: '₽',
        imgUrl: 'url',
        category: 'Электроника',
    },
    {
        id: 2,
        name: 'Bershka',
        description: 'T-short',
        price: 14,
        priceSymbol: '₽',
        imgUrl: 'url',
        category: 'Одежда',
    },
    {
        id: 3,
        name: 'H&M',
        description: 'Trousers',
        price: 15,
        priceSymbol: '₽',
        imgUrl: 'url',
        category: 'Одежда',
    },
    {
        id: 4,
        name: 'Bershka',
        description: 'Hat',
        price: 10,
        priceSymbol: '₽',
        imgUrl: 'url',
        category: 'Одежда',
    }
]

const clothes = products.filter((p) => p.category == 'Одежда');
const getPriceFn = (value: number, symbol: PriceSymbol = '₽'): string =>
    `${value.toLocaleString('ru-RU')} ${symbol}`;

afterEach(jest.clearAllMocks);

jest.useFakeTimers().setSystemTime(new Date(2023, 0, 1, 3, 0, 0, 0));

jest.mock('../../utils/getPrice', () => {
    return {
        __esModule: true,
        getPrice: jest.fn((value: number, symbol: PriceSymbol = '₽'): string =>
            getPriceFn(value, symbol)
        ),
    };
});

jest.mock('../../utils/updateCategories', () => {
    return {
        __esModule: true,
        updateCategories: jest.fn(
            (currentCategories: Category[], changedCategories: Category): Category[] => {
                return currentCategories
            }
        ),
    };
});

jest.mock('../../hooks/useProducts', () => {
    return {
        __esModule: true,
        useProducts: jest.fn(() => products),
    };
});

describe('test MainPage', () => {
    it('should render correctly', () => {
        const rendered = render(
            <MainPage/>
        );
        expect(rendered.asFragment()).toMatchSnapshot();
    });
    it('should call update category', () => {
        const rendered = render(
            <MainPage/>
        );

        expect(updateCategories).toHaveBeenCalledTimes(0);
        fireEvent.click(rendered.getByText('Для дома'));
        expect(updateCategories).toHaveBeenCalledTimes(1);

        const renderedProducts = rendered.baseElement.getElementsByClassName('product-card');
        Array.from(renderedProducts).forEach((p, i) => {
            const card = p.getElementsByClassName('product-card__text')[0];
            expect(card.getElementsByClassName('product-card__name')[0].textContent).toStrictEqual(products[i].name)
            expect(card.getElementsByClassName('product-card__description')[0].textContent).toStrictEqual(products[i].description)
            expect(card.getElementsByClassName('product-card__category')[0].textContent).toStrictEqual(products[i].category)
            expect(card.getElementsByClassName('product-card__price')[0].textContent).toStrictEqual(getPriceFn(products[i].price, products[i].priceSymbol));
        });
    });
});
