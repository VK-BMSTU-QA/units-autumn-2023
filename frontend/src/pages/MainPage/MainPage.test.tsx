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
]

afterEach(jest.clearAllMocks);

jest.useFakeTimers().setSystemTime(new Date(2023, 0, 1, 3, 0, 0, 0));

jest.mock('../../utils/getPrice', () => {
    return {
        __esModule: true,
        getPrice: jest.fn((value: number, symbol: PriceSymbol = '₽'): string =>
            `${value.toLocaleString('ru-RU')} ${symbol}`
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
    });
});