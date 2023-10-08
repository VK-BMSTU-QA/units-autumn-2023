import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('test update categories function', () => {
    const categories: Category[] = [];

    it('should return update currentCategories with changedCategories', () => {
        expect(updateCategories(categories, 'Электроника')).toEqual([
            'Электроника',
        ]);
        expect(updateCategories(categories, 'Одежда')).toEqual(['Одежда']);
        expect(updateCategories(categories, 'Электроника')).toEqual([
            'Электроника',
        ]);
        categories.push('Одежда');
        expect(updateCategories(categories, 'Одежда')).toEqual([]);
    });
});
