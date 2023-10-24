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
    const productTShirt = createProduct(1, 'Футболка', 'Одежда');
    const productPentium = createProduct(2, 'Pentium G4560', 'Электроника');
    const productCoat = createProduct(3, 'Куртка', 'Одежда');
    const productCleaner = createProduct(4, 'Пылесос', 'Для дома');
    const productXeon = createProduct(5, 'Xeon E31220', 'Электроника');

    it('should apply empty categories to empty products', () => {
        expect(applyCategories([], [])).toStrictEqual([]);
    });

    it('should apply empty categories', () => {
        expect(
            applyCategories([productTShirt, productPentium, productCleaner], [])
        ).toStrictEqual([productTShirt, productPentium, productCleaner]);
    });

    it('should apply to empty products', () => {
        expect(applyCategories([], ['Одежда'])).toStrictEqual([]);
    });

    test.each<[Product[], Category[], Product[]]>([
        [[productTShirt], ['Для дома'], []],
        [[productTShirt, productPentium], ['Для дома'], []],
        [[productTShirt], ['Одежда'], [productTShirt]],
        [[productTShirt], ['Одежда', 'Для дома'], [productTShirt]],
        [
            [
                productTShirt,
                productPentium,
                productCoat,
                productCleaner,
                productXeon,
            ],
            ['Одежда'],
            [productTShirt, productCoat],
        ],
        [
            [productTShirt, productPentium],
            ['Одежда', 'Для дома'],
            [productTShirt],
        ],
        [
            [
                productTShirt,
                productPentium,
                productCoat,
                productCleaner,
                productXeon,
            ],
            ['Одежда', 'Для дома'],
            [productTShirt, productCoat, productCleaner],
        ],
    ])(
        'should apply categories correct: [%s, %s] to %s',
        (products, categories, expected) => {
            expect(applyCategories(products, categories)).toStrictEqual(
                expected
            );
        }
    );
});
