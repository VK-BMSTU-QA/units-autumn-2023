import { useProducts } from '../../hooks';
import { Category } from '../../types';
import { applyCategories } from '../applyCategories';
import {updateCategories} from "../updateCategories";

describe('tests for updateCategories function', () => {
    const allCategories: Category[] = ['Одежда', 'Для дома', 'Электроника'];
    it('should update categories', () => {
        expect(updateCategories(allCategories, 'Электроника')).toEqual(allCategories.slice(0,2));
        expect(updateCategories([], 'Электроника')).toEqual(['Электроника']);
        expect(updateCategories(allCategories.slice(0,2), 'Электроника')).toEqual(allCategories);
    });
});
