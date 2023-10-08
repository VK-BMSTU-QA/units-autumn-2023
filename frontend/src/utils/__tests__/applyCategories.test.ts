import {useProducts} from '../../hooks';
import {Category} from '../../types';
import {applyCategories} from '../applyCategories';

describe('tests for applyCategories function', () => {
    const allCategories: Category[] = ['Одежда', 'Для дома', 'Электроника'];
    const allPoruducts = useProducts();
    it('should return products by category', () => {
        expect(applyCategories(allPoruducts, allCategories)).toEqual(allPoruducts);
        expect(applyCategories(allPoruducts, [allCategories[1]])).toEqual(allPoruducts[1]);
        expect(applyCategories(allPoruducts, allCategories.slice(1, 3))).toEqual(allPoruducts);
        expect(applyCategories(allPoruducts, [])).toEqual(allPoruducts);
    });
});
