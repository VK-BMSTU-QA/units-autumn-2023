import '@testing-library/jest-dom';

import React from 'react';

import { fireEvent, render } from '@testing-library/react';

import * as useCurrentTimeHookModule from '../../hooks/useCurrentTime';
import * as applyCategoriesUtilsModule from '../../utils/applyCategories';
import * as updateCategoriesUtilsModule from '../../utils/updateCategories';
import { MainPage } from './MainPage';

const mockUseCurrentTime = jest.spyOn(
    useCurrentTimeHookModule,
    'useCurrentTime'
);
mockUseCurrentTime.mockReturnValue('12:00.00');

const mockApplyCategories = jest.spyOn(
    applyCategoriesUtilsModule,
    'applyCategories'
);
const mockUpdateCategories = jest.spyOn(
    updateCategoriesUtilsModule,
    'updateCategories'
);

afterEach(jest.clearAllMocks);

describe('MainPage test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call useCurrentTime once on create', () => {
        render(<MainPage />);

        expect(mockUseCurrentTime).toHaveBeenCalledTimes(1);
    });

    it('should update selected categories on category click', () => {
        const rendered = render(<MainPage />);

        expect(mockUpdateCategories).toHaveBeenCalledTimes(0);

        fireEvent.click(rendered.getAllByText('Одежда')[0]);

        expect(mockUpdateCategories).toHaveBeenCalledTimes(1);

        fireEvent.click(rendered.getAllByText('Одежда')[0]);

        expect(mockUpdateCategories).toHaveBeenCalledTimes(2);
    });

    it('should apply categories to products on category click', () => {
        const rendered = render(<MainPage />);

        expect(mockApplyCategories).toHaveBeenCalledTimes(1);
        expect(
            rendered.container.getElementsByClassName(
                'categories__badge_selected'
            )
        ).toHaveLength(0);

        fireEvent.click(rendered.getAllByText('Электроника')[0]);
        expect(mockApplyCategories).toHaveBeenCalledTimes(2);
        expect(
            rendered.container.getElementsByClassName('product-card')
        ).toHaveLength(2);
        expect(
            rendered.container.getElementsByClassName(
                'categories__badge_selected'
            )
        ).toHaveLength(1);
        expect(rendered.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(rendered.getByText('Принтер')).toBeInTheDocument();
        expect(rendered.queryByText('Костюм гуся')).not.toBeInTheDocument();

        fireEvent.click(rendered.getAllByText('Электроника')[0]);
        expect(mockApplyCategories).toHaveBeenCalledTimes(3);
        expect(
            rendered.container.getElementsByClassName(
                'categories__badge_selected'
            )
        ).toHaveLength(0);
    });
});
