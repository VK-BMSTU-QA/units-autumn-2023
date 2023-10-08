import { act } from 'react-dom/test-utils';
import { useCurrentTime } from '../useCurrentTime';
import { renderHook, cleanup } from '@testing-library/react';

jest.spyOn(global, 'setTimeout');

describe('test use current time', () => {
    beforeEach(() => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date('2017-01-01T03:01:02'));
    });

    afterAll(() => {
        jest.useRealTimers();
    });

    it('should return to be 2017 01 01', () => {
        const date = new Date('2017-01-01T03:01:02');
        const timeElement = renderHook(useCurrentTime);

        expect(timeElement.result.current).toBe(
            date.toLocaleTimeString('ru-RU')
        );
    });

    it('should call function after time', () => {
        const date = new Date('2017-01-01T03:01:02');
        date.setSeconds(date.getSeconds() + 1);

        const timeElement = renderHook(useCurrentTime);
        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(timeElement.result.current).toBe(
            date.toLocaleTimeString('ru-RU')
        );
    });
});
