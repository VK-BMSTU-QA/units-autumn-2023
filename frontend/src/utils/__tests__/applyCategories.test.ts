import { Product } from '../../types';
import { applyCategories } from '../applyCategories';

// TODO: beforeEach
describe('test apply categories function', () => {
    it('return all products', () => {
        let products: Product[] = [
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
        ];

        expect(applyCategories(products, [])).toStrictEqual(products);
    });

    it('should filter products', () => {
        let products: Product[] = [
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

        let expected: Product[] = [
            {
                id: 1,
                name: 'Iphone',
                description: '',
                category: 'Электроника',
                price: 10,
            },
        ];

		expect(applyCategories(products, ['Электроника'])).toStrictEqual(expected)
    });
});
