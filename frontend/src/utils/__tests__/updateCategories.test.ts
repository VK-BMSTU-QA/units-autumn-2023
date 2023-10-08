import {Category} from "../../types";
import {updateCategories} from "../updateCategories";

describe('test update categories function', () => {
    const categories: Category[] = [
        'Электроника',
        'Для дома',
        'Одежда'
    ]

    it('should add category to current categories if it was not in current categories before', () => {
        expect(updateCategories(['Электроника', 'Для дома'], 'Одежда')).toStrictEqual(categories);
        expect(updateCategories(['Для дома'], 'Электроника')).toStrictEqual(['Для дома', 'Электроника']);
    });

    it('should remove category from current categories if it was in current categories before', () => {
        expect(updateCategories(['Электроника', 'Для дома'], 'Электроника')).toStrictEqual(['Для дома']);
        expect(updateCategories(['Для дома'], 'Для дома')).toStrictEqual([]);
    });
});
