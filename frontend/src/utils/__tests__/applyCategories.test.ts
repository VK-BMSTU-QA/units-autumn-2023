import { applyCategories } from '../applyCategories';
import type { Category, Product } from '../../types';

describe('test apply categories function', () => {
    const products: Product[] = [
        { id: 1, name: 'Product 1', description: 'Description 1', price: 100, category: 'Электроника' },
        { id: 2, name: 'Product 2', description: 'Description 2', price: 200, category: 'Для дома' },
        { id: 3, name: 'Product 3', description: 'Description 3', price: 300, category: 'Одежда' },
        { id: 4, name: 'Product 4', description: 'Description 4', price: 400, category: 'Электроника' },
    ];

    const categories: Category[] = ['Электроника', 'Для дома'];

    it('should return products with selected categories', () => {
        const result = applyCategories(products, categories);
        expect(result).toEqual([
            { id: 1, name: 'Product 1', description: 'Description 1', price: 100, category: 'Электроника' },
            { id: 2, name: 'Product 2', description: 'Description 2', price: 200, category: 'Для дома' },
            { id: 4, name: 'Product 4', description: 'Description 4', price: 400, category: 'Электроника' },
        ]);
    });

    it('should return all products if no categories are selected', () => {
        const result = applyCategories(products, []);
        expect(result).toEqual(products);
    });

    it('should return empty array if no products match the selected categories', () => {
        const result = applyCategories(products, []);
        expect(result).toEqual(products);
    });
});

