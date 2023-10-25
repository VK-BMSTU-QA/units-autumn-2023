import { Category } from "../../types";
import { updateCategories } from "../updateCategories";

describe('test update categories function', () => {
    const all_categories: Category[] = ['Электроника', 'Для дома', 'Одежда'];

    it('should exclude electronics', () => {
        expect(updateCategories(all_categories, 'Электроника'))
            .toStrictEqual(['Для дома', 'Одежда'])
    });

    it('should add clothes', () => {
        expect(updateCategories(['Электроника', 'Для дома'], 'Одежда'))
            .toStrictEqual(all_categories)
    });
});
