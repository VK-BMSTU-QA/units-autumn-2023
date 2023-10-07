import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';

afterEach(jest.clearAllMocks);

describe('Main page test', () => {
    jest.spyOn(Date.prototype, 'toLocaleTimeString').mockReturnValue(
        '14:00:00'
    );
	
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});
