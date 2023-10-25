import '@testing-library/jest-dom' 
import { MainPage } from '../MainPage'
import React from 'react'

import {render, fireEvent} from '@testing-library/react'
// import { useProducts } from '../../../hooks'
import * as useProducts from '../../../hooks/useProducts'
import * as updateCategories  from '../../../utils/updateCategories'
import * as useCurrentTime from '../../../hooks/useCurrentTime'
import * as applyCatgegories from '../../../utils/applyCategories'

afterEach(jest.clearAllMocks)

jest.spyOn(useCurrentTime, 'useCurrentTime').mockReturnValue('00:00:00')
const mockApplyCategories = jest.spyOn(applyCatgegories, 'applyCategories')
mockApplyCategories.mockReturnValue(useProducts.useProducts())
const mockUpdateCategories = jest.spyOn(updateCategories, 'updateCategories')
mockUpdateCategories.mockReturnValue(['Одежда', 'Электроника'])

const getCards = (rendered) => rendered.container.getElementsByClassName('product-card')

describe('main page test', () => {
    it('should render main page correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered).toMatchSnapshot();
    })
        
    it('should call updateCategories and applyCategory function when category is clicked', () => {
        const rendered = render(<MainPage />)

        expect(mockUpdateCategories).toBeCalledTimes(0);
        expect(mockApplyCategories).toBeCalledTimes(1);

        expect(getCards(rendered)).toHaveLength(1);

        fireEvent.click(rendered.baseElement.getElementsByClassName('categories__badge')[0]);
        expect(mockUpdateCategories).toBeCalledTimes(1);
        expect(mockApplyCategories).toBeCalledTimes(2);
        expect(getCards(rendered)).toHaveLength(1);

    })
})
