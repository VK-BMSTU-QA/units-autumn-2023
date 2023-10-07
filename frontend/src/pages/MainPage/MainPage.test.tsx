import { MainPage } from "./MainPage";
import { fireEvent, render } from "@testing-library/react";
import '@testing-library/jest-dom';
import { useCurrentTime} from '../../hooks';
import { updateCategories } from '../../utils';

afterEach(jest.clearAllMocks);

jest.mock('../../hooks/useCurrentTime', () => {
    return {
        __esModule: true,
        useCurrentTime: jest.fn(() => '00:00:00'),
    };
});

jest.mock('../../utils/updateCategories', () => {
    return {
        __esModule: true,
        updateCategories: jest.fn(() => ['Электроника']),
    };
});

describe('test MainPage', () => {
    it('correct render', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
        expect(useCurrentTime).toHaveBeenCalledTimes(1);
        expect(updateCategories).toHaveBeenCalledTimes(0);
    });

    it('update categories on click', () => {
        const rendered = render(<MainPage />);
        const electronicsButton= rendered.baseElement.getElementsByClassName('categories__badge')[0];

        expect(updateCategories).toHaveBeenCalledTimes(0);
        fireEvent.click(electronicsButton);
        expect(updateCategories).toHaveBeenCalledTimes(1);
    });
});