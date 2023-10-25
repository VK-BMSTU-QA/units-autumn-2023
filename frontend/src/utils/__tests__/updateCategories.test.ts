import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('updateCategories', () => {
    it('removes existing category from current', () => {
        const categories: Category[] = ['Одежда', 'Для дома'];

        const res = updateCategories(categories, 'Одежда');

        expect(res).toHaveLength(1);
        expect(res).toContain('Для дома');
    });

    it('adds a category to current', () => {
        const categories: Category[] = ['Одежда', 'Для дома'];

        const res = updateCategories(categories, 'Электроника');

        const expectedCategories = ['Одежда', 'Для дома', 'Электроника'];

        expect(res).toStrictEqual(expectedCategories);
    });
});
