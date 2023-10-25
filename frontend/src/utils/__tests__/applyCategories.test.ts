import { useProducts } from '../../hooks';
import type { Category } from '../../types';
import { applyCategories } from '../applyCategories';

describe('test apply categories function', () => {
    const products = useProducts()
    const categories: Category[] = ['Электроника', 'Для дома', 'Одежда']

    it('should return products from these categories with changes', () => {
        expect(applyCategories(products, [categories[0], categories[1]])).toEqual([
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Latest iphone, buy it now',
                price: 999,
                priceSymbol: '$',
                category: 'Электроника',
                imgUrl: '/iphone.png',
            },
            {
                id: 3,
                name: 'Настольная лампа',
                description: 'Говорят, что ее использовали в pixar',
                price: 699,
                category: 'Для дома',
                imgUrl: '/lamp.png',
            },
            {
                id: 4,
                name: 'Принтер',
                description: 'Незаменимая вещь для студента',
                price: 7000,
                category: 'Электроника',
            },
        ]);
    });

    it('should return products from these categories without changes', () => {
        expect(applyCategories(products, [])).toEqual(products);
        expect(applyCategories(products, categories)).toEqual(products);
    });
});
