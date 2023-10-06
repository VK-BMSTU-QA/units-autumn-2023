import { applyCategories } from '../applyCategories';
import { Product } from '../../types/Product';
import { Category } from '../../types/Category';

const makeTestProduct = (id: number, category: Category): Product => {
    return {
        id: id,
        category: category,
        name: '',
        description: '',
        price: 0,
    };
};

const testProducts: Product[] = [
    makeTestProduct(0, 'Электроника'),
    makeTestProduct(1, 'Для дома'),
    makeTestProduct(2, 'Одежда'),
];

describe('applyCategories', () => {
    it('processes empty categories', () => {
        expect(applyCategories(testProducts, [])).toBe(testProducts);
    });

    it('filters products by category', () => {
        const res = applyCategories(testProducts, ['Электроника', 'Одежда']);
        expect(res.length).toStrictEqual(2);

        expect(res).toContain(testProducts[0]);
        expect(res).toContain(testProducts[2]);

        expect(res).not.toContain(testProducts[1]);
    });
});
