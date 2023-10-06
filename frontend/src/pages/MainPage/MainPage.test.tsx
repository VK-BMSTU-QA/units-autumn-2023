import { fireEvent, render } from "@testing-library/react";
import '@testing-library/jest-dom';
import { MainPage } from "./MainPage";
import * as currentTimeHook from "../../hooks/useCurrentTime"
import * as applyCategoriesUtil from "../../utils/applyCategories"

const mockCurrentTime = jest.spyOn(currentTimeHook, 'useCurrentTime');
mockCurrentTime.mockReturnValue('16:10:15')

const mockApplyCategories = jest.spyOn(applyCategoriesUtil, 'applyCategories');

const findNodeWithText = (nodes: HTMLCollection, text: string) => {
    for (const node of nodes) {
        if (node.textContent === text)
            return node;
    }

    return undefined;
}

afterEach(jest.clearAllMocks);
describe('Main page test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage/>);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call updateCategories on category click', () => {
        const {container} = render(<MainPage/>);

        const categoryButtons = container.getElementsByClassName('categories__badge');
        const clothButton = findNodeWithText(categoryButtons, 'Одежда');

        expect(clothButton).not.toBeUndefined;

        expect(mockApplyCategories).toHaveBeenCalledTimes(1);
        fireEvent.click(clothButton!);
        expect(mockApplyCategories).toHaveBeenCalledTimes(2);
    });
});
