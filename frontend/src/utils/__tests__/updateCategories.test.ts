import { updateCategories } from '../updateCategories';
import type { Category, Product } from '../../types';

interface TestCase {
    nameOfTest: string;
    currentCat: Category[];
    changedCat: Category;
    expected: Category[];
}

describe('test update category', () => {
    const testCases: TestCase[] = [
        {
            nameOfTest: 'All categories not checked',
            currentCat: [],
            changedCat: 'Для дома',
            expected: ['Для дома'],
        },
        {
            nameOfTest: 'Remove category',
            currentCat: ['Для дома', 'Электроника', 'Одежда'],
            changedCat: 'Для дома',
            expected: ['Электроника', 'Одежда'],
        },
        {
            nameOfTest: 'One category checked and not given',
            currentCat: ['Для дома'],
            changedCat: 'Одежда',
            expected: ['Для дома', 'Одежда'],
        },
        {
            nameOfTest: 'Remove only one category',
            currentCat: ['Для дома'],
            changedCat: 'Для дома',
            expected: [],
        },
    ];

    test.each(testCases)(
        'Update: $nameOfTest',
        ({ nameOfTest, currentCat, changedCat, expected }) => {
            expect(updateCategories(currentCat, changedCat)).toStrictEqual(
                expected
            );
        }
    );
});
