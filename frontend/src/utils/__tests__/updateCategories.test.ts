import { Category } from "../../types";
import { updateCategories } from "../updateCategories";

const getTestCategories = (): Category[] => {
    return [
        "Одежда",
        "Для дома",
    ];
};

describe("updateCategories", () => {
    it("removes existing category from current", () => {
        const res = updateCategories(getTestCategories(), "Одежда");
        
        expect(res).toHaveLength(1);
        expect(res).toContain("Для дома");
    })

    it("adds a category to current", () => {
        const res = updateCategories(getTestCategories(), "Электроника");
        
        expect(res).toHaveLength(3);

        expect(res[0]).toStrictEqual("Одежда");
        expect(res[1]).toStrictEqual("Для дома");
        expect(res[2]).toStrictEqual("Электроника");
    })
});
