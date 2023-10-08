import {updateCategories} from "../updateCategories";

describe('test update categories function', () => {
  it('should add category in list', () => {
    expect(updateCategories(['Электроника'], 'Для дома')).toEqual(['Электроника', 'Для дома']);
    expect(updateCategories(['Одежда'], 'Для дома')).toEqual(['Одежда', 'Для дома']);
  });

  it('should remove category from the list', () => {
    expect(updateCategories(['Электроника', 'Для дома', 'Одежда'], 'Для дома')).toEqual(['Электроника', 'Одежда']);
    expect(updateCategories(['Электроника'], 'Электроника')).toEqual([]);
  });
});
