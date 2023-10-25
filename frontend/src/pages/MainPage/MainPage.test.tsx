import { fireEvent, render } from "@testing-library/react";
import '@testing-library/jest-dom';
import { MainPage } from "./MainPage";
import * as currentTimeHook from "../../hooks/useCurrentTime"
import * as applyCategoriesUtil from "../../utils/applyCategories"
import * as updateCategoriesUtil from "../../utils/updateCategories"

const mockCurrentTime = jest.spyOn(currentTimeHook, 'useCurrentTime');
mockCurrentTime.mockReturnValue('16:10:15')

const mockApplyCategories = jest.spyOn(applyCategoriesUtil, 'applyCategories');
const mockUpdateCategories = jest.spyOn(updateCategoriesUtil, 'updateCategories')

afterEach(jest.clearAllMocks);
describe('Main page test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage/>);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call applyCategories on category click', async () => {
        const rendered = render(<MainPage/>);

        const clothButton = await rendered.findByTestId('pc-Электроника')
        expect(clothButton).not.toBeUndefined;

        expect(mockApplyCategories).toHaveBeenCalledTimes(1);

        expect(rendered.container.getElementsByClassName('categories__badge_selected')).toHaveLength(0);

        fireEvent.click(clothButton);
        
        expect(mockApplyCategories).toHaveBeenCalledTimes(2);

        expect(rendered.container.getElementsByClassName('product-card')).toHaveLength(2);
        expect(rendered.container.getElementsByClassName('categories__badge_selected')).toHaveLength(1);

        expect(rendered.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(rendered.getByText('Принтер')).toBeInTheDocument();
        expect(rendered.queryByText('Костюм гуся')).not.toBeInTheDocument();
    });

    it('should call updateCategories on category click', async () => {
        const rendered = render(<MainPage/>);

        const clothButton = await rendered.findByTestId('pc-Одежда')
        expect(clothButton).not.toBeUndefined;

        expect(mockUpdateCategories).toHaveBeenCalledTimes(0);
        fireEvent.click(clothButton!);
        expect(mockUpdateCategories).toHaveBeenCalledTimes(1);
    });
});
