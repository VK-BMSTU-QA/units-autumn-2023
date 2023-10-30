import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    function isEqualCategories(res: Category[], test: Category[]) {
        return res.every((val, i) => {
            return val === test[i];
        });
    }

    it('should return correct updated categories with empty currentCategories', () => {
        const resultCategories = updateCategories([], 'Электроника');

        expect(
            isEqualCategories(resultCategories, ['Электроника'])
        ).toStrictEqual(true);
    });

    it('should return correct updated categories when changedCategories is included in currentCategories', () => {
        const resultCategories = updateCategories(
            ['Электроника', 'Для дома'],
            'Электроника'
        );

        expect(isEqualCategories(resultCategories, ['Для дома'])).toStrictEqual(
            true
        );
    });

    it('should return correct updated categories when changedCategories is not included in currentCategories', () => {
        const resultCategories = updateCategories(
            ['Электроника', 'Для дома'],
            'Одежда'
        );

        expect(
            isEqualCategories(resultCategories, [
                'Электроника',
                'Для дома',
                'Одежда',
            ])
        ).toStrictEqual(true);
    });
});
