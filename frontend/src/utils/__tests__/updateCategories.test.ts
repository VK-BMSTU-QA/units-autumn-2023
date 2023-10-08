import {Category} from '../../types';
import {updateCategories} from "../updateCategories";

describe('test update categories function', () => {
  it('should remove categories from the list', () => {
    const categories: Category[] = ['Электроника', 'Для дома', 'Одежда']
    expect(updateCategories(categories, 'Для дома')).toEqual(['Электроника', 'Одежда']);
    expect(updateCategories(categories, 'Электроника')).toEqual(['Для дома', 'Одежда']);
  });

  it('should remove categories with dublicates', () => {
    const categories: Category[] = ['Электроника', 'Электроника', 'Для дома', 'Одежда', 'Для дома']
    expect(updateCategories(categories, 'Для дома')).toEqual(['Электроника', 'Электроника', 'Одежда']);
    expect(updateCategories(categories, 'Электроника')).toEqual(['Для дома', 'Одежда', 'Для дома']);
  });

  it('should add category', () => {
    expect(updateCategories(['Электроника', 'Одежда'], 'Для дома')).toEqual(['Электроника', 'Одежда', 'Для дома']);
    expect(updateCategories(['Электроника'], 'Одежда')).toEqual(['Электроника', 'Одежда']);
  });
});
