import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    test.each<[Category[], Category, Category[]]>([
        [['Одежда'], 'Одежда', []],
        [['Одежда', 'Для дома'], 'Для дома', ['Одежда']],
        [
            ['Электроника', 'Для дома', 'Одежда'],
            'Для дома',
            ['Электроника', 'Одежда'],
        ],
    ])(
        'should remove categories correct and in the right order: [%s, %s] to %s',
        (categories, category, expected) => {
            expect(updateCategories(categories, category)).toStrictEqual(
                expected
            );
        }
    );

    test.each<[Category[], Category, Category[]]>([
        [[], 'Одежда', ['Одежда']],
        [['Одежда'], 'Для дома', ['Одежда', 'Для дома']],
        [
            ['Электроника', 'Для дома'],
            'Одежда',
            ['Электроника', 'Для дома', 'Одежда'],
        ],
    ])(
        'should add categories correct and in the right order: [%s, %s] to %s',
        (categories, category, expected) => {
            expect(updateCategories(categories, category)).toStrictEqual(
                expected
            );
        }
    );

    it('should check unexpected inputs', () => {
        expect(updateCategories(['Одежда', 'Одежда'], 'Одежда')).toStrictEqual(
            [] as Category[]
        );

        expect(
            updateCategories(
                ['Электроника', 'Для дома', 'Для дома'],
                'Для дома'
            )
        ).toStrictEqual(['Электроника'] as Category[]);
    });
});
