import { applyCategories } from '../applyCategories';
import type { Category, Product } from '../../types';

const table: Array<[Product[], Category[], Product[]]> = [
    [
        [
            {
                id: 1,
                name: 'MacBook',
                description: 'M2',
                price: 1400,
                priceSymbol: '₽',
                imgUrl: 'url',
                category: 'Электроника',
            },
            {
                id: 2,
                name: 'Bershka',
                description: 'T-short',
                price: 14,
                priceSymbol: '₽',
                imgUrl: 'url',
                category: 'Одежда',
            },

        ],
        [
            'Одежда',
        ],
        [
            {
                id: 2,
                name: 'Bershka',
                description: 'T-short',
                price: 14,
                priceSymbol: '₽',
                imgUrl: 'url',
                category: 'Одежда',
            },
        ]
    ],
    [
        [],
        ['Одежда'],
        []
    ],
    [
        [],
        [],
        []
    ],
    [
        [
            {
                id: 1,
                name: 'MacBook',
                description: 'M2',
                price: 1400,
                priceSymbol: '₽',
                imgUrl: 'url',
                category: 'Электроника',
            },
            {
                id: 2,
                name: 'Bershka',
                description: 'T-short',
                price: 14,
                priceSymbol: '₽',
                imgUrl: 'url',
                category: 'Одежда',
            },

        ],
        [],
        [
            {
                id: 1,
                name: 'MacBook',
                description: 'M2',
                price: 1400,
                priceSymbol: '₽',
                imgUrl: 'url',
                category: 'Электроника',
            },
            {
                id: 2,
                name: 'Bershka',
                description: 'T-short',
                price: 14,
                priceSymbol: '₽',
                imgUrl: 'url',
                category: 'Одежда',
            },
        ]
    ],
];

test.each(table)('all products with categories $', (products, categories, expected) => {
    expect(applyCategories(products, categories)).toStrictEqual(expected);
});