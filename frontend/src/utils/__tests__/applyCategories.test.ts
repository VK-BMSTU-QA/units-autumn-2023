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
    ]

    it('should leavy only clothes', () => {
        expect(applyCategories(products, ['Одежда'])).toStrictEqual([products[1], products[2]])
    })
})
