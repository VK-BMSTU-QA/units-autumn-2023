import { applyCategories } from '../applyCategories';

describe('test get price function', () => {
    it('should return value with price symbol', () => {
        expect(applyCategories(100, '₽')).toBe('100 ₽');
        expect(applyCategories(325, '$')).toBe('325 $');
    });
});