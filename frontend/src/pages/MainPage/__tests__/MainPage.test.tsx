import '@testing-library/jest-dom' 
import { MainPage } from '../MainPage'
import React from 'react'

import {render, fireEvent} from '@testing-library/react'
import { useCurrentTime, useProducts } from '../../../hooks'
import { updateCategories } from '../../../utils'

afterEach(jest.clearAllMocks)

jest.mock('../../../hooks', () => {
    
    const originalModule = jest.requireActual('../../../hooks');

    return {
        __esModule: true,
        ...originalModule,
        useCurrentTime: jest.fn(() => {return '00:00:00'}),
    };
});

jest.mock('../../../utils', () => {
    
    const originalModule = jest.requireActual('../../../utils')

    return {
        __esModule: true,
        ...originalModule,
        updateCategories: jest.fn(() => ['Одежда', 'Электроника']),
        applyCategories: jest.fn(() => useProducts())
    }
})

describe('main page test', () => {
    it('should render main page correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered).toMatchSnapshot();
    })
        
    it('should call updateCategories and applyCategory function when category is clicked', () => {
        const rendered = render(<MainPage />)

        expect(updateCategories).toBeCalledTimes(0);
        expect(updateCategories).toBeCalledTimes(0);
        fireEvent.click(rendered.baseElement.getElementsByClassName('categories__badge')[0]);
        expect(updateCategories).toBeCalledTimes(1);
        expect(updateCategories).toBeCalledTimes(1);
    })
})