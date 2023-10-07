import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';

import { applyCategories } from '../../utils';

afterEach(jest.clearAllMocks);

jest.mock('../../utils', () => {
    const original = jest.requireActual('../../utils');
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
        applyCategories: jest.fn().mockReturnValue(products),
    };
});

describe('Main page test', () => {
    it('should render correctly', () => {
        jest.spyOn(Date.prototype, 'toLocaleTimeString').mockReturnValueOnce(
            '14:00:00'
        );

        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call applyCategories callback when category click', () => {
        const rendered = render(<MainPage />);

        expect(applyCategories).toHaveBeenCalledTimes(1);
        fireEvent.click(
            rendered.container.getElementsByClassName('categories__badge')[0]
        );
        expect(applyCategories).toHaveBeenCalledTimes(2);
    });
});
