import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    const categories: Category[] = ['Для дома', 'Одежда', 'Электроника']

    it('should return the updated categories with the addition of a new one', () => {
        expect(updateCategories([], categories[0])).toEqual([categories[0]]);
    });

    it('should return the updated categories with the removal of one', () => {
        expect(updateCategories(categories, categories[0])).toEqual([categories[1], categories[2]]);
        expect(updateCategories([categories[0], categories[1]], categories[0])).toEqual([categories[1]]);
    });
});
