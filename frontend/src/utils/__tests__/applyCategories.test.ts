import {applyCategories} from '../applyCategories';
import {Product, Category} from "../../types";

describe('test applyCategories', () => {
    const products: Product[] = [
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
        }
    ];

    const categories: Category[] = [... new Set(products.map (product => product.category))];

    it('should return products with chosen filters', () => {
        expect(applyCategories(products, categories)).toStrictEqual(products);
        expect(applyCategories(products, ['Для дома'])).toStrictEqual([products[2]]);
        expect(applyCategories(products, ['Электроника', 'Одежда'])).toStrictEqual([products[0], products[1], products[3]]);
    });

    it('should return all products when no categories provided', () => {
        expect(applyCategories(products, [])).toStrictEqual(products);
    });
});
