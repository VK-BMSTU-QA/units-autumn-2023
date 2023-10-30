import type {Category} from '../../types';
import {updateCategories} from '../updateCategories';


const table: Array<[string, Category[], Category, Category[]]> = [
    [
        'remove category',
        ['Для дома', 'Одежда', 'Электроника'],
        'Электроника',
        ['Для дома', 'Одежда']
    ],
    [
        'add category',
        ['Для дома', 'Электроника'],
        'Одежда',
        ['Для дома', 'Электроника', 'Одежда']
    ],
    [
        'add first category',
        [],
        'Электроника',
        ['Электроника']
    ],
    [
        'delete last category',
        ['Электроника'],
        'Электроника',
        []
    ]
]

test.each(table)('%s', (_, categories, changedcategory, expected) => {
    expect(updateCategories(categories, changedcategory)).toStrictEqual(expected);
});
