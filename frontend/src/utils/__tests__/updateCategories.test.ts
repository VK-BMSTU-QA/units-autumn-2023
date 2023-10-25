import { updateCategories } from "../updateCategories"
import { Category } from "../../types"

describe('test update categories function', () => {
    it('should return categories without changed', () => {
        const catHome: Category = 'Для дома'
        const catCloth: Category = 'Одежда'
        const catElectronic: Category = 'Электроника'
        
        expect(updateCategories([catHome, catCloth, catElectronic], catHome)).toStrictEqual([catCloth, catElectronic])
    })

    it('should return categories with changed', () => {
        const catHome: Category = 'Для дома'
        const catCloth: Category = 'Одежда'
        const catElectronic: Category = 'Электроника'

        expect(updateCategories([catHome, catCloth], catElectronic)).toStrictEqual([catHome, catCloth, catElectronic])
    })
})
