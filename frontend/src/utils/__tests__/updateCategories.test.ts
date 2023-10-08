import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('test update categories function', () => {
    const categories: Category[] = [];

    it('should return update currentCategories with changedCategories', () => {
        expect(updateCategories(categories, 'Электроника')).toBe([
            'Электроника',
        ]);
        expect(updateCategories(categories, 'Одежда')).toBe([
            'Электроника',
            'Одежда',
        ]);
        expect(updateCategories(categories, 'Электроника')).toBe(['Одежда']);
        expect(
            updateCategories(categories, 'Странная категория ни к месту' as Category)
        ).toBe(['Одежда']);
    });
});
