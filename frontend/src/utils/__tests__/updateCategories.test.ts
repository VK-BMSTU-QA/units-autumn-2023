import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('test update categories function', () => {
    it('should add category to not empty array', () => {
        let currentCategories: Category[] = ['Для дома', 'Одежда'];
        let changedCategory: Category = 'Электроника';
        let result: Category[] = ['Для дома', 'Одежда', 'Электроника'];
        expect(updateCategories(currentCategories, changedCategory)).toStrictEqual(result);
    });

    it('should add category to empty array', () => {
        let currentCategories: Category[] = [];
        let changedCategory: Category = 'Одежда';
        let result: Category[] = ['Одежда'];
        expect(updateCategories(currentCategories, changedCategory)).toStrictEqual(result);
    });

    it('should remove category', () => {
        let currentCategories: Category[] = ['Для дома', 'Одежда'];
        let changedCategory: Category = 'Одежда';
        let result: Category[] = ['Для дома'];
        expect(updateCategories(currentCategories, changedCategory)).toStrictEqual(result);
    });
});
