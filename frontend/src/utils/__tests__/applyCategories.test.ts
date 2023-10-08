import { applyCategories } from '../applyCategories';
import { Product } from '../../types';
import { useProducts } from '../../hooks';

describe('test get price function', () => {
    const products: Product[] = useProducts();

    it('should return value with price symbol', () => {
        expect(applyCategories(products, ['Электроника'])).toEqual([
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
                id: 4,
                name: 'Принтер',
                description: 'Незаменимая вещь для студента',
                price: 7000,
                category: 'Электроника',
            },
        ]);
        expect(
            applyCategories(products, ['Электроника', 'Для дома', 'Одежда'])
        ).toEqual(products);
        expect(applyCategories(products, ['Для дома', 'Одежда'])).toEqual([
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
        ]);
    });
});
