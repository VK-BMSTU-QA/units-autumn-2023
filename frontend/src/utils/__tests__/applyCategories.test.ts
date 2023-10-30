import { useProducts } from '../../hooks';
import { Product } from '../../types';
import { applyCategories } from '../applyCategories';

describe('test update categories function', () => {
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
        },
    ];

    function getCheckProduct(resProd: Product[]) {
        return (p: Product, i: number) => {
            expect(p.name).toStrictEqual(resProd[i].name);
            expect(p.description).toStrictEqual(resProd[i].description);
            expect(p.category).toStrictEqual(resProd[i].category);
            expect(p.price).toStrictEqual(resProd[i].price);
            expect(p.priceSymbol).toStrictEqual(resProd[i].priceSymbol);
        };
    }

    it('should return array with all products', () => {
        const resultProducts = products;
        const checkProduct = getCheckProduct(resultProducts);

        applyCategories(products, []).forEach(checkProduct);
    });

    it('should return array with filtered products', () => {
        const resultProducts: Product[] = [
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
        ];
        const checkProduct = getCheckProduct(resultProducts);

        applyCategories(products, ['Электроника']).forEach(checkProduct);
    });
});
