import { applyCategories } from "../applyCategories";
import { Category, Product } from "../../types";

describe('test apply categories function', () => {
    let last_id = 0;
    const createDummyProduct = (name: string, category: Category) => (
        {
            id: ++last_id,
            name,
            category,
            description: `description #${last_id}`,
            price: 1000
        }
    )

    const products: Product[] = [
        createDummyProduct('Телефон', 'Электроника'),
        createDummyProduct('Костюм енота', 'Одежда'),
        createDummyProduct('Кепка', 'Одежда'),
        createDummyProduct('Лампа', 'Для дома')
    ];

    const electronics = [products[0]];
    const clothes = [products[1], products[2]];
    const home_appliances = [products[3]];

    it('should only leave clothes', () => {
        expect(applyCategories(products, ['Одежда'])).toStrictEqual(clothes);
    });

    it('should only leave electronics', () => {
        expect(applyCategories(products, ['Электроника'])).toStrictEqual(electronics);
    });

    it('should only leave home appliances', () => {
        expect(applyCategories(products, ['Для дома'])).toStrictEqual(home_appliances);
    });

    it('should leave clothes and electronics', () => {
        expect(applyCategories(products, ['Одежда', 'Электроника'])).toStrictEqual([...electronics, ...clothes]);
    });

    it('should leave electronics and home appliances', () => {
        expect(applyCategories(products, ['Электроника', 'Для дома'])).toStrictEqual([...electronics, ...home_appliances]);
    });

    it('should leave clothes and home appliances', () => {
        expect(applyCategories(products, ['Одежда', 'Для дома'])).toStrictEqual([...clothes, ...home_appliances]);
    });

    it('should leave all products', () => {
        expect(applyCategories(products, [])).toStrictEqual(products);
        expect(applyCategories(products, ['Одежда', 'Электроника', 'Для дома'])).toStrictEqual(products);
    });

})
