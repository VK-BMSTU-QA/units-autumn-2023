import { updateCategories } from "../updateCategories"
import { Category } from "../../types"

describe('test update categories function', () => {
    it('should return categories without changed', () => {
        const cat1: Category = 'Для дома'
        const cat2: Category = 'Одежда'
        const cat3: Category = 'Электроника'
        
        expect(updateCategories([cat1, cat2, cat3], cat1)).toStrictEqual([cat2, cat3])
    })

    it('should return categories with changed', () => {
        const cat1: Category = 'Для дома'
        const cat2: Category = 'Одежда'
        const cat3: Category = 'Электроника'

        expect(updateCategories([cat1, cat2], cat3)).toStrictEqual([cat1, cat2, cat3])
    })
})
