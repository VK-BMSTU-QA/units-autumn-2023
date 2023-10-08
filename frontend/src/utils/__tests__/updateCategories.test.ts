import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    const categories: Category[] = ['Для дома', 'Одежда', 'Электроника']

    it('should return update categories', () => {
        expect(updateCategories([], categories[0])).toEqual([categories[0]]);
        expect(updateCategories(categories, categories[0])).toEqual(categories.slice(1, 3));
        expect(updateCategories(categories.slice(0, 2), categories[0])).toEqual([categories[1]]);
    });


});