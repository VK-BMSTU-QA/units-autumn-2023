import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('test update categories function', () => {
    let currentCategories: Category[];

    beforeEach(() => {
        currentCategories = ['Для дома', 'Одежда'];
    });

    it('should add category', () => {
        let result: Category[] = [...currentCategories, ];
        expect(updateCategories(currentCategories, 'Электроника')).toStrictEqual(['Для дома', 'Одежда', 'Электроника']);
    });

    it('should remove category', () => {
        expect(updateCategories(currentCategories, 'Одежда')).toStrictEqual(['Для дома']);
    });
});
