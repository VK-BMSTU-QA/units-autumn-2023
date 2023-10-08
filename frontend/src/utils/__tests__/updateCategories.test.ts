import { updateCategories } from '../updateCategories';
import type { Category, Product } from '../../types';

describe('test update categories function', () => {
    const currentCategories: Category[] = ['Электроника', 'Для дома'];

    it('should remove category if it already exists in current categories', () => {
        const changedCategory: Category = 'Для дома';
        const result = updateCategories(currentCategories, changedCategory);
        expect(result).toEqual(['Электроника']);
    });

    it('should add category if it does not exist in current categories', () => {
        const changedCategory: Category = 'Одежда';
        const result = updateCategories(currentCategories, changedCategory);
        expect(result).toEqual(['Электроника', 'Для дома', 'Одежда']);
    });

    it('should return empty array if current categories is empty', () => {
        const currentCategories: Category[] = [];
        const changedCategory: Category = 'Одежда';
        const result = updateCategories(currentCategories, changedCategory);
        expect(result).toEqual(['Одежда']);
    });
});
