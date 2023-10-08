import { MainPage } from "./MainPage";
import { fireEvent, render } from "@testing-library/react";
import '@testing-library/jest-dom';
import { useCurrentTime} from '../../hooks';
import { updateCategories } from '../../utils';

afterEach(jest.clearAllMocks);

jest.mock('../../hooks/useCurrentTime', () => {
    return {
        useCurrentTime: jest.fn(() => '12:00:00'),
    };
});

jest.mock('../../utils/updateCategories', () => {
    return {
        updateCategories: jest.fn(() => ['Для дома']),
    };
});

describe('tests for MainPage', () => {
    it('Render test(without time)', () => {
        const MyPageRendered = render(<MainPage />);
        expect(MyPageRendered.asFragment()).toMatchSnapshot();
        expect(useCurrentTime).toHaveBeenCalledTimes(1);
    });
    it('Render test(time only)', () => {
        const MyPageRendered = render(<MainPage />);
        expect(useCurrentTime).toHaveBeenCalledTimes(1);
    });
    it('Render test(with time)', () => {
        const MyPageRendered = render(<MainPage />);
        expect(MyPageRendered.asFragment()).toMatchSnapshot();
        expect(useCurrentTime).toHaveBeenCalledTimes(1);
    });
    it('Apply category call check', () => {
        const MyPageRendered = render(<MainPage />);
        fireEvent.click(
            MyPageRendered.baseElement.getElementsByClassName(
                'categories__badge'
            )[1]
        );
        expect(updateCategories).toHaveBeenCalledTimes(1);
    });
});
