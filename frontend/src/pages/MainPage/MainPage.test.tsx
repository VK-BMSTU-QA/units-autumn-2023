import { MainPage } from "./MainPage";
import { fireEvent, render } from "@testing-library/react";
import '@testing-library/jest-dom';
import { useCurrentTime } from '../../hooks';
import { updateCategories } from '../../utils';
import { PriceSymbol, Product } from '../../types';

const products: Product[] = [
    {
        id: 1,
        name: 'test1',
        description: 'test1',
        price: 10000,
        priceSymbol: '$',
        category: 'Электроника',
    },
    {
        id: 2,
        name: 'test2',
        description: 'test2',
        price: 2,
        priceSymbol: '$',
        category: 'Для дома',
    },
    {
        id: 3,
        name: 'test3',
        description: 'test3',
        price: 3,
        priceSymbol: '$',
        category: 'Одежда',
    },
    {
        id: 4,
        name: 'еще одна электроника',
        description: 'дада электроника!',
        price: 4000,
        priceSymbol: '$',
        category: 'Электроника',
    },
]

const electronicProducts = products.filter((p) => p.category == 'Электроника');
const getPriceFn = (value: number, symbol: PriceSymbol = '₽'): string =>
    `${value.toLocaleString('ru-RU')} ${symbol}`;

afterEach(jest.clearAllMocks);

jest.mock('../../hooks/useCurrentTime', () => {
    return {
        __esModule: true,
        useCurrentTime: jest.fn(() => '00:00:00'),
    };
});

jest.mock('../../utils/updateCategories', () => {
    return {
        __esModule: true,
        updateCategories: jest.fn(() => ['Электроника']),
    };
});

jest.mock('../../hooks/useProducts', () => {
    return {
        __esModule: true,
        useProducts: jest.fn(() => products),
    };
});

jest.mock('../../utils/getPrice', () => {
    return {
        __esModule: true,
        getPrice: jest.fn(
            (value: number, symbol: PriceSymbol = '₽'): string =>
                getPriceFn(value, symbol)
        ),
    }
});

describe('test MainPage', () => {
    it('correct render', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
        expect(useCurrentTime).toHaveBeenCalledTimes(1);
        expect(updateCategories).toHaveBeenCalledTimes(0);
    });

    it('update categories on click', () => {
        const rendered = render(<MainPage />);
        const electronicsButton = rendered.baseElement.getElementsByClassName('categories__badge')[0];

        expect(updateCategories).toHaveBeenCalledTimes(0);
        fireEvent.click(electronicsButton);
        expect(updateCategories).toHaveBeenCalledTimes(1);

        const renderedProducts = rendered.baseElement.getElementsByClassName('product-card');
        Array.from(renderedProducts).forEach((p, i) => {
            const card = p.getElementsByClassName('product-card__text')[0];
            expect(card.getElementsByClassName('product-card__name')[0].textContent).toStrictEqual(electronicProducts[i].name)
            expect(card.getElementsByClassName('product-card__description')[0].textContent).toStrictEqual(electronicProducts[i].description)
            expect(card.getElementsByClassName('product-card__category')[0].textContent).toStrictEqual(electronicProducts[i].category)
            expect(card.getElementsByClassName('product-card__price')[0].textContent).toStrictEqual(getPriceFn(electronicProducts[i].price, electronicProducts[i].priceSymbol));
        });
    });
});
