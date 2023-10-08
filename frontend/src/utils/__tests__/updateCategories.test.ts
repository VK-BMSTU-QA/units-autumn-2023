import { Category } from "../../types";
import {updateCategories} from "../updateCategories";

describe('test updateCategories', () => {
    const allCategories: Category[] = ['Электроника', 'Для дома', 'Одежда']

    it('should push back non-existing category into categories', () => {
        expect(updateCategories(allCategories.slice(0, 2), allCategories[2])).toEqual(allCategories);
        expect(updateCategories([], allCategories[1])).toEqual([allCategories[1]]);
    });

    it('should remove existing category from categories', () => {
        expect(updateCategories(allCategories, allCategories[0])).toEqual(allCategories.slice(1, 3));
        expect(updateCategories([allCategories[0]], allCategories[0])).toEqual([]);
    });
});
