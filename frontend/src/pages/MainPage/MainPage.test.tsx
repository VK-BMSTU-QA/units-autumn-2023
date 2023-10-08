import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import * as currentTimeHook from "../../hooks/useCurrentTime"

const mockCurrentTime = jest.spyOn(currentTimeHook, 'useCurrentTime');
mockCurrentTime.mockReturnValue('20:58:28')

afterEach(jest.clearAllMocks);
describe('MainPages test', () => {
    it('should render correctly', () => {
        const rendered = render(< MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    test('Display category cards when category button "Одежда" is clicked', () => {
      const mainPage = render(<MainPage />);
      
        const categoryButton = mainPage.getByText('Одежда', {selector: '.categories__badge'});
      
        expect(mainPage.queryByText('Принтер')).not.toBeNull();
        expect(mainPage.queryByText('Настольная лампа')).not.toBeNull();
      
        fireEvent.click(categoryButton);
      
        expect(mainPage.queryByText('Костюм гуся')).toBeInTheDocument();
        expect(mainPage.queryByText('Принтер')).toBeNull();
        expect(mainPage.queryByText('Настольная лампа')).toBeNull();

        fireEvent.click(categoryButton);

        expect(mainPage.queryByText('Принтер')).not.toBeNull();
        expect(mainPage.queryByText('Настольная лампа')).not.toBeNull();
    });

    test('Display category cards when category buttons "Для дома", "Электроника" is clicked', () => {
      const mainPage = render(<MainPage />);
      
        const categoryButton1 = mainPage.getByText('Для дома', {selector: '.categories__badge'});
        const categoryButton2 = mainPage.getByText('Электроника', {selector: '.categories__badge'});
      
        expect(mainPage.queryByText('Костюм гуся')).toBeInTheDocument();
        expect(mainPage.queryByText('Принтер')).toBeInTheDocument();
        expect(mainPage.queryByText('Настольная лампа')).toBeInTheDocument();
      
        fireEvent.click(categoryButton1);
        fireEvent.click(categoryButton2);
      
        expect(mainPage.queryByText('Костюм гуся')).toBeNull();
        expect(mainPage.queryByText('Принтер')).toBeInTheDocument();
        expect(mainPage.queryByText('Настольная лампа')).toBeInTheDocument();
    });
});
