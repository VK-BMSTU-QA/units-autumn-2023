import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    it('should add new category', () => {
        let current: Category[] = ['Электроника'];
        let expected: Category[] = ['Электроника', 'Для дома'];
        expect(updateCategories(current, 'Для дома')).toStrictEqual(expected);
    });

    it('should delete category', () => {
        let current: Category[] = [
            'Электроника',
            'Для дома',
            'Одежда',
            'Электроника',
        ];

        let expected: Category[] = ['Для дома', 'Одежда'];
        expect(updateCategories(current, 'Электроника')).toStrictEqual(
            expected
        );
    });
});
