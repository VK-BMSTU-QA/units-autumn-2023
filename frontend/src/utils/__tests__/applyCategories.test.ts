import { applyCategories } from '../applyCategories';
import { Product } from '../../types/Product';
import { Category } from '../../types/Category';

const makeTestProduct = (
    id: number,
    category: Category,
    name = '',
    description = '',
    price = 0
): Product => {
    return {
        id: id,
        category: category,
        name: name,
        description: description,
        price: price,
    };
};

describe('applyCategories', () => {
    it('handles empty categories', () => {
        const products = [
            makeTestProduct(0, 'Электроника'),
            makeTestProduct(1, 'Для дома'),
            makeTestProduct(2, 'Одежда'),
        ];

        expect(applyCategories(products, [])).toStrictEqual(products);
    });

    it('filters products by category', () => {
        const products = [
            makeTestProduct(0, 'Электроника'),
            makeTestProduct(1, 'Для дома'),
            makeTestProduct(2, 'Одежда'),
        ];

        const res = applyCategories(products, ['Электроника', 'Одежда']);

        const expectedProducts = [
            makeTestProduct(0, 'Электроника'),
            makeTestProduct(2, 'Одежда'),
        ];

        expect(res).toStrictEqual(expectedProducts);
    });

    it('returns same products if you pass all categories', () => {
        const getProducts = () => [
            makeTestProduct(0, 'Электроника'),
            makeTestProduct(1, 'Для дома'),
            makeTestProduct(2, 'Одежда'),
        ];

        const products = getProducts();

        const res = applyCategories(products, [
            'Электроника',
            'Одежда',
            'Для дома',
        ]);

        expect(res).toStrictEqual(getProducts());
    });
});
