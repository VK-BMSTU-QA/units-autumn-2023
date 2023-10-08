import React from 'react';
import { MainPage } from './MainPage';
import { fireEvent, render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { useCurrentTime } from '../../hooks/useCurrentTime';

afterEach(jest.clearAllMocks);

jest.mock('../../hooks/useCurrentTime', () => {
    return {
        __esModule: true,
        useCurrentTime: jest.fn(() => '11:11:11'),
    };
});

describe('test MainPage', () => {
    it('correct render', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();

        expect(useCurrentTime).toHaveBeenCalledTimes(1);
    });

    it('correct time', () => {
        const rendered = render(<MainPage />);

        const time = rendered.baseElement.getElementsByTagName('h3')[0];
        expect(time.textContent).toEqual('11:11:11');
    });

    it('update categories on click', () => {
        const rendered = render(<MainPage />);

        const products =
            rendered.baseElement.getElementsByClassName('product-card');
        expect(products.length).toEqual(4);

        const clothesButton =
            rendered.baseElement.getElementsByClassName('categories__badge')[0];
        fireEvent.click(clothesButton);

        expect(products.length).toEqual(1);
    });
});
