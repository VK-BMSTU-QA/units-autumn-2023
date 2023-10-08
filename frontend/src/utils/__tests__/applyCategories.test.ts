import {applyCategories} from '../applyCategories';
import {Category, Product} from '../../types';

describe('test apply categories function', () => {
    const products: Product[] = [
        {
            id: 1,
            name: '',
            description: '',
            price: 0,
            category: 'Электроника',
        },
        {
            id: 2,
            name: '',
            description: '',
            price: 0,
            category: 'Для дома',
        },
        {
            id: 3,
            name: '',
            description: '',
            price: 0,
            category: 'Одежда',
        },
        {
            id: 4,
            name: '',
            description: '',
            price: 0,
            category: 'Для дома',
        },
    ]

    it('should return only products with category "Для дома"', () => {
        const categories: Category[] = ['Для дома']
        const productWithAplliedCategories: Product[] = [
            {
                id: 2,
                name: '',
                description: '',
                price: 0,
                category: 'Для дома',
            },
            {
                id: 4,
                name: '',
                description: '',
                price: 0,
                category: 'Для дома',
            },
        ]

        expect(applyCategories(products, categories)).toEqual(productWithAplliedCategories);
    });

    it('should return all products', () => {
        const categories: Category[] = ['Электроника', 'Для дома', 'Одежда']

        expect(applyCategories(products, categories)).toEqual(products);
    });

    it('should return products as they are', () => {
        const categories: Category[] = []
        expect(applyCategories(products, categories)).toEqual(products);
    });
});