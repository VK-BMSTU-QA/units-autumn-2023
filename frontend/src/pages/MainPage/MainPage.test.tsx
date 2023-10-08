import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import '@testing-library/jest-dom/extend-expect';
import { MainPage } from './MainPage';
import { updateCategories } from '../../utils';

jest.mock('../../utils/updateCategories', () => {
    return {
        __esModule: true,
        updateCategories: jest.fn(() => ['Одежда']),
    };
});

afterEach(jest.clearAllMocks);
describe('MainPage test', () => {
    const date = new Date('2019-05-14T11:01:58.135Z');
    jest
        .spyOn(global, 'Date')
        .mockImplementation(() => date);

    it('should render correctly', () => {

        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should add title', () => {
        const rendered = render(<MainPage />);

        expect(rendered.getByText('VK Маркет')).toHaveClass(
            'main-page__title'
        );
    });

    it('should add element for time', () => {
        const rendered = render(<MainPage />);

        expect(rendered.getByText('14:01:58')).toBeInTheDocument();
    });

    it('should add categories', () => {
        const rendered = render(<MainPage />);

        expect(rendered.container.getElementsByClassName('categories').length).toBe(1);
    });

    it('should add products', () => {
        const rendered = render(<MainPage />);

        expect(rendered.container.getElementsByClassName('product-card').length).toBe(4);
    });

    it('should call update categories when category click', () => {
        const rendered = render(<MainPage />);

        expect(updateCategories).toHaveBeenCalledTimes(0);
        fireEvent.click(rendered.container.getElementsByClassName('categories__badge')[0]);
        expect(updateCategories).toHaveBeenCalledTimes(1);
    });
});
