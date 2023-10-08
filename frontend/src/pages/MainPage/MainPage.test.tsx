import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';

afterEach(jest.clearAllMocks);

jest.mock('../../hooks/', () => {
    const original = jest.requireActual('../../hooks');
    const products = [
        {
            id: 1,
            name: 'Iphone',
            description: '',
            category: 'Электроника',
            price: 10,
        },
        {
            id: 2,
            name: 'Cap',
            description: '',
            category: 'Одежда',
            price: 5,
        },
        {
            id: 3,
            name: 'Pants',
            description: '',
            category: 'Одежда',
            price: 5,
        },
        {
            id: 4,
            name: 'Диван',
            description: '',
            category: 'Для дома',
            price: 20,
        },
    ];
    return {
        ...original,
        useCurrentTime: jest.fn().mockReturnValue('14:00:00'),
        useProducts: jest.fn().mockReturnValue(products),
    };
});

describe('Main page test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should update products when category click', () => {
        const rendered = render(<MainPage />);

        expect(
            rendered.container.querySelectorAll('.product-card').length
        ).toBe(4);

        fireEvent.click(
            rendered.container.querySelectorAll('.categories__badge')[0]
        );

        expect(
            rendered.container.querySelectorAll('.product-card').length
        ).toBe(2);
    });
});
