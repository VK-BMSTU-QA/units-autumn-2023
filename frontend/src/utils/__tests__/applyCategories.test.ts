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
    it('should return product matching only chosen category', () => {

        const prodCloth = newTestProduct('Одежда')
        const prodHome = newTestProduct('Для дома')

        expect(applyCategories([prodCloth, prodHome], ['Одежда'])).toStrictEqual([prodCloth]);
        
    })
    
    it('should return all products', () => {
        const prodCloth = newTestProduct('Одежда')
        const prodHome = newTestProduct('Для дома')

        expect(applyCategories([prodCloth, prodHome], ['Одежда', 'Для дома'])).toStrictEqual([prodCloth, prodHome]);
        expect(applyCategories([prodCloth, prodHome], [])).toStrictEqual([prodCloth, prodHome]);
    })
})
