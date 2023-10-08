import { applyCategories } from '../applyCategories';
import type { Category, Product } from '../../types';

interface TestCase {
    nameOfTest: string;
    pr: Product[];
    cat: Category[];
    expected: Product[];
}
function createProduct(id: number, name: string, category: Category): Product {
    return {
        id,
        name,
        description: name + name,
        price: id,
        category,
    };
}

describe('test apply categories function', () => {
    const testCases: TestCase[] = [
        {
            nameOfTest: 'Check for empty products',
            pr: [],
            cat: ['Для дома'],
            expected: [],
        },
        {
            nameOfTest: 'Check for empty category',
            pr: [
                createProduct(1, 'str', 'Для дома'),
                createProduct(2, 'str', 'Одежда'),
                createProduct(3, 'str', 'Электроника'),
            ],
            cat: [],
            expected: [
                createProduct(1, 'str', 'Для дома'),
                createProduct(2, 'str', 'Одежда'),
                createProduct(3, 'str', 'Электроника'),
            ],
        },
        {
            nameOfTest: 'Only 1 category',
            pr: [
                createProduct(1, 'str', 'Для дома'),
                createProduct(2, 'str2', 'Одежда'),
                createProduct(3, 'str', 'Электроника'),
            ],
            cat: ['Для дома'],
            expected: [createProduct(1, 'str', 'Для дома')],
        },
        {
            nameOfTest: 'All categories',
            pr: [
                createProduct(1, 'str', 'Для дома'),
                createProduct(1, 'str', 'Для дома'),
                createProduct(2, 'str2', 'Одежда'),
                createProduct(3, 'str', 'Электроника'),
            ],
            cat: ['Для дома', 'Одежда', 'Электроника'],
            expected: [
                createProduct(1, 'str', 'Для дома'),
                createProduct(1, 'str', 'Для дома'),
                createProduct(2, 'str2', 'Одежда'),
                createProduct(3, 'str', 'Электроника'),
            ],
        },
    ];

    test.each(testCases)(
        'Apply category $s',
        ({ nameOfTest, pr, cat, expected }) => {
            expect(applyCategories(pr, cat)).toStrictEqual(expected);
        }
    );
});
