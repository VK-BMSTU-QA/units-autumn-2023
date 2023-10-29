import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    it('should return array with category "Электроника"', () => {
        expect(updateCategories([], 'Электроника').join(' ')).toBe(
            'Электроника'
        );
    });

    it('should return array with category "Для дома"', () => {
        expect(
            updateCategories(['Электроника', 'Для дома'], 'Электроника').join(
                ' '
            )
        ).toBe('Для дома');
    });

    it('should return with category "Электроника Для дома Одежда"', () => {
        expect(
            updateCategories(['Электроника', 'Для дома'], 'Одежда').join(' ')
        ).toBe('Электроника Для дома Одежда');
    });
});
