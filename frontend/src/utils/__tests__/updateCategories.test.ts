import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    it('should return array with filtered categories', () => {
        expect(
            updateCategories(['Электроника', 'Для дома'], 'Электроника').join(
                ' '
            )
        ).toBe('Для дома');

        expect(
            updateCategories(['Электроника', 'Для дома'], 'Одежда').join(' ')
        ).toBe('Электроника Для дома Одежда');
    });
});
