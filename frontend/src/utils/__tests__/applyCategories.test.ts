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

const makeTestProducts = (): Product[] => [
    makeTestProduct(0, 'Электроника'),
    makeTestProduct(1, 'Для дома'),
    makeTestProduct(2, 'Одежда'),
];

describe('applyCategories', () => {
    it('handles empty categories', () => {
        expect(applyCategories(makeTestProducts(), [])).toStrictEqual(
            makeTestProducts()
        );
    });

    it('filters products by category', () => {
        const res = applyCategories(makeTestProducts(), [
            'Электроника',
            'Одежда',
        ]);
        expect(res).toHaveLength(2);

        const testProducts = makeTestProducts();

        expect(res[0]).toStrictEqual(testProducts[0]);
        expect(res[1]).toStrictEqual(testProducts[2]);
    });
});
