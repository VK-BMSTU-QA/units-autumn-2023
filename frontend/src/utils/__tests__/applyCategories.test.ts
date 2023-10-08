import { Category, Product } from "../../types"
import { applyCategories } from "../applyCategories"


describe('test applyCategories function', () => {
    it('should return product list matching selected categories', () => {
        const rightCat: Category = "Одежда"
        const wrongCat: Category = "Для дома"

        const rightProd: Product = {
            id: 1,
            name: '',
            description: '',
            price: 0,
            category: rightCat
        }
        const wrongProd: Product = {
            id: 1,
            name: '',
            description: '',
            price: 0,
            category: wrongCat
        }

        expect(applyCategories([rightProd, wrongProd], [rightCat])).toStrictEqual([rightProd]);
        expect(applyCategories([rightProd, wrongProd], [rightCat, wrongCat])).toStrictEqual([rightProd, wrongProd]);
        expect(applyCategories([rightProd, wrongProd], [])).toStrictEqual([rightProd, wrongProd]);
    })
})