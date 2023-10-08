import { Category, PriceSymbol, Product } from '../../types';
import { applyCategories } from '../applyCategories';

const createProduct = (
    id: number,
    name: string,
    category: Category,
    description = '',
    price = 0,
    priceSymbol?: PriceSymbol,
    imgUrl?: string
): Product => ({
    id,
    name,
    description,
    price,
    priceSymbol,
    imgUrl,
    category,
});

describe('test apply categories function', () => {
    it('should return empty array of products', () => {
        const product1 = createProduct(1, 'Футболка', 'Одежда');
        const product2 = createProduct(2, 'Pentium G4560', 'Электроника');

        expect(applyCategories([], [])).toStrictEqual([]);

        expect(applyCategories([], ['Одежда'])).toStrictEqual([]);

        expect(applyCategories([product1], ['Для дома'])).toStrictEqual([]);

        expect(applyCategories([product2], ['Для дома'])).toStrictEqual([]);

        expect(
            applyCategories([product1, product2], ['Для дома'])
        ).toStrictEqual([]);
    });

    it('should return array with single product', () => {
        const product1 = createProduct(1, 'Футболка', 'Одежда');
        const product2 = createProduct(2, 'Pentium G4560', 'Электроника');

        expect(applyCategories([product1], ['Одежда'])).toStrictEqual([
            product1,
        ]);

        expect(
            applyCategories([product1], ['Одежда', 'Для дома'])
        ).toStrictEqual([product1]);

        expect(
            applyCategories([product2], ['Электроника', 'Для дома'])
        ).toStrictEqual([product2]);

        expect(applyCategories([product1, product2], ['Одежда'])).toStrictEqual(
            [product1]
        );

        expect(
            applyCategories([product1, product2], ['Одежда', 'Для дома'])
        ).toStrictEqual([product1]);
    });

    it('should return array with multi products', () => {
        const product1 = createProduct(1, 'Футболка', 'Одежда');
        const product2 = createProduct(2, 'Pentium G4560', 'Электроника');
        const product3 = createProduct(3, 'Куртка', 'Одежда');
        const product4 = createProduct(4, 'Пылесос', 'Для дома');
        const product5 = createProduct(5, 'Xeon E31220', 'Электроника');

        expect(
            applyCategories(
                [product1, product2, product3, product4, product5],
                ['Одежда']
            )
        ).toStrictEqual([product1, product3]);

        expect(
            applyCategories(
                [product1, product2, product3, product4, product5],
                ['Электроника']
            )
        ).toStrictEqual([product2, product5]);

        expect(
            applyCategories(
                [product1, product2, product3, product4, product5],
                ['Одежда', 'Для дома']
            )
        ).toStrictEqual([product1, product3, product4]);
    });
});
