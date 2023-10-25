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
jest.spyOn(applyCatgegories, 'applyCategories').mockReturnValue(useProducts.useProducts())
jest.spyOn(updateCategories, 'updateCategories').mockReturnValue(['Одежда', 'Электроника'])
const mockUseProducts = jest.spyOn(useProducts, 'useProducts');

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
