import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';

import { MainPage } from '../MainPage';

describe('Categories test', () => {
    it('should render correctly', () => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date('2017-01-01T03:01:02'));

        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
        jest.useRealTimers();
    });

    it('should render products with category', () => {
        const rendered = render(<MainPage />);

        const lenAllProducts =
            rendered.container.getElementsByClassName('product-card').length;

        fireEvent.click(rendered.getAllByText('Одежда')[0]);

        const lenClothesProducts =
            rendered.container.getElementsByClassName('product-card').length;

        expect(lenClothesProducts).toBeLessThan(lenAllProducts);
    });
});
