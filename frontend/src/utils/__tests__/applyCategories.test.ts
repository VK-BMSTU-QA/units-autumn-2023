import {useProducts} from '../../hooks';
import {Category, Product} from '../../types';
import {applyCategories} from '../applyCategories';

describe('tests for applyCategories function', () => {
    const allCategories: Category[] = ['Одежда', 'Для дома', 'Электроника'];
    const allProducts: Product[] = [
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
            id: 2,
            name: 'Костюм гуся',
            description: 'Запускаем гуся, работяги',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
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
    ];

    it('should return products by category', () => {
        expect(applyCategories(allProducts, allCategories)).toEqual(
            allProducts
        );
        expect(applyCategories(allProducts, [allCategories[1]])).toEqual([
            allProducts[2],
        ]);
        expect(applyCategories(allProducts, allCategories.slice(1, 3))).toEqual([allProducts[0], ...allProducts.slice(2)]);
        expect(applyCategories(allProducts, [])).toEqual(allProducts);
    });
});
