import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';

afterEach(jest.clearAllMocks);
describe('Main page test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should add class for selected badge', () => {
        const rendered = render(<MainPage />);

        expect(rendered.getByText('Одежда')).toHaveClass(
            'categories__badge_selected'
        );
        expect(rendered.getByText('Электроника')).not.toHaveClass(
            'categories__badge_selected'
        );
        expect(rendered.getByText('Для дома')).not.toHaveClass(
            'categories__badge_selected'
        );
    });

    it('should call callback when category click', () => {
        const onCategoryClick = jest.fn();
        const rendered = render(<MainPage />);

        expect(onCategoryClick).toHaveBeenCalledTimes(0);
        fireEvent.click(rendered.getByText('Одежда'));
        expect(onCategoryClick).toHaveBeenCalledTimes(1);
    });
});
