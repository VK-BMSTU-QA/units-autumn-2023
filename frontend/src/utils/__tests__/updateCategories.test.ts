import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    it('should return empty array', () => {
        expect(updateCategories(['Одежда'], 'Одежда')).toStrictEqual([]);

        expect(updateCategories(['Для дома'], 'Для дома')).toStrictEqual([]);

        expect(updateCategories(['Электроника'], 'Электроника')).toStrictEqual(
            []
        );
    });

    it('should return array with single category', () => {
        expect(updateCategories([], 'Одежда')).toStrictEqual([
            'Одежда',
        ] as Category[]);

        expect(updateCategories([], 'Для дома')).toStrictEqual([
            'Для дома',
        ] as Category[]);

        expect(updateCategories([], 'Электроника')).toStrictEqual([
            'Электроника',
        ] as Category[]);
    });

    it('should add to non empty categories array', () => {
        expect(updateCategories(['Одежда'], 'Для дома')).toStrictEqual([
            'Одежда',
            'Для дома',
        ] as Category[]);

        expect(
            updateCategories(['Электроника', 'Для дома'], 'Одежда')
        ).toStrictEqual(['Электроника', 'Для дома', 'Одежда'] as Category[]);
    });

    it('should remove single item from categories array then len > 1', () => {
        expect(
            updateCategories(['Одежда', 'Для дома'], 'Для дома')
        ).toStrictEqual(['Одежда'] as Category[]);

        expect(
            updateCategories(['Электроника', 'Для дома', 'Одежда'], 'Для дома')
        ).toStrictEqual(['Электроника', 'Одежда'] as Category[]);
    });

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
