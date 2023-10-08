import { Product } from '../../types';
import { applyCategories } from '../applyCategories';

describe('test apply categories function', () => {
    let products: Product[] = [];

    beforeEach(() => {
        products = [
            {
                id: 1,
                name: 'Iphone',
                description: '',
                category: 'Электроника',
                price: 10,
            },
            {
                id: 2,
                name: 'Cap',
                description: '',
                category: 'Одежда',
                price: 5,
            },
            {
                id: 3,
                name: 'Pants',
                description: '',
                category: 'Одежда',
                price: 5,
            },
        ];
    });

    it('should return all products', () => {
        let expected = [...products];

        expect(applyCategories(products, [])).toStrictEqual(expected);
    });

    it('should filter products', () => {
        let expected: Product[] = [
            {
                id: 1,
                name: 'Iphone',
                description: '',
                category: 'Электроника',
                price: 10,
            },
        ];

        expect(applyCategories(products, ['Электроника'])).toStrictEqual(
            expected
        );
    });
});
