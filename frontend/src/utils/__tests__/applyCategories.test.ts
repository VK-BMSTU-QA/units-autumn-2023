import { Category, Product } from "../../types"
import { applyCategories } from "../applyCategories"


const newTestProduct = (
    category: Category, id: number=1, name:string = '', description:string = '',
    price: number = 0
) => ({
    id: id,
    name: name,
    description: description,
    price: price,
    category: category,
})

describe('test applyCategories function', () => {
    it('should return product list matching selected categories', () => {

        const prod1 = newTestProduct('Одежда')
        const prod2 = newTestProduct('Для дома')

        expect(applyCategories([prod1, prod2], ['Одежда'])).toStrictEqual([prod1]);
        expect(applyCategories([prod1, prod2], ['Одежда', 'Для дома'])).toStrictEqual([prod1, prod2]);
        expect(applyCategories([prod1, prod2], [])).toStrictEqual([prod1, prod2]);
    })
})
