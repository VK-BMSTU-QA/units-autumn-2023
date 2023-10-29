import { useProducts } from '../../hooks';
import { Product } from '../../types';
import { applyCategories } from '../applyCategories';

describe('test update categories function', () => {
    let resultProducts = useProducts();

    function checkProduct(p: Product, i: number) {
        expect(p.name).toStrictEqual(resultProducts[i].name);
        expect(p.description).toStrictEqual(resultProducts[i].description);
        expect(p.category).toStrictEqual(resultProducts[i].category);
        expect(p.price).toStrictEqual(resultProducts[i].price);
        expect(p.priceSymbol).toStrictEqual(resultProducts[i].priceSymbol);
    }

    it('should return array with all products', () => {
        applyCategories(useProducts(), []).forEach(checkProduct);
    });

    it('should return array with filtered products', () => {
        resultProducts = [
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

        applyCategories(useProducts(), ['Электроника']).forEach(checkProduct);
    });
});
