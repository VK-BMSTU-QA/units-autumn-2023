import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test updateCategories', () => {
    const allCategories: Category[] = ['Электроника', 'Для дома', 'Одежда'];

    it('del category from all', () => {
        expect(updateCategories(allCategories, 'Электроника')).toEqual([
            'Для дома',
            'Одежда',
        ]);
    });

    it('add category if not in list', () => {
        expect(updateCategories(['Электроника', 'Для дома'], 'Одежда')).toEqual(
            allCategories
        );
    });
});