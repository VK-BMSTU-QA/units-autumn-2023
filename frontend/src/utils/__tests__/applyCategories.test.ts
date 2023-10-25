import {applyCategories} from '../applyCategories';
import type {Category, Product} from '../../types';

// const table: Array<[Product[], Category[], Product[]]> = [
//     [
//         [
//             {
//                 id: 1,
//                 name: 'MacBook',
//                 description: 'M2',
//                 price: 1400,
//                 priceSymbol: '₽',
//                 imgUrl: 'url',
//                 category: 'Электроника',
//             },
//             {
//                 id: 2,
//                 name: 'Bershka',
//                 description: 'T-short',
//                 price: 14,
//                 priceSymbol: '₽',
//                 imgUrl: 'url',
//                 category: 'Одежда',
//             },

//         ],
//         [
//             'Одежда',
//         ],
//         [
//             {
//                 id: 2,
//                 name: 'Bershka',
//                 description: 'T-short',
//                 price: 14,
//                 priceSymbol: '₽',
//                 imgUrl: 'url',
//                 category: 'Одежда',
//             },
//         ]
//     ],
//     [
//         [],
//         ['Одежда'],
//         []
//     ],
//     [
//         [],
//         [],
//         []
//     ],
//     [
//         [
//             {
//                 id: 1,
//                 name: 'MacBook',
//                 description: 'M2',
//                 price: 1400,
//                 priceSymbol: '₽',
//                 imgUrl: 'url',
//                 category: 'Электроника',
//             },
//             {
//                 id: 2,
//                 name: 'Bershka',
//                 description: 'T-short',
//                 price: 14,
//                 priceSymbol: '₽',
//                 imgUrl: 'url',
//                 category: 'Одежда',
//             },

//         ],
//         [],
//         [
//             {
//                 id: 1,
//                 name: 'MacBook',
//                 description: 'M2',
//                 price: 1400,
//                 priceSymbol: '₽',
//                 imgUrl: 'url',
//                 category: 'Электроника',
//             },
//             {
//                 id: 2,
//                 name: 'Bershka',
//                 description: 'T-short',
//                 price: 14,
//                 priceSymbol: '₽',
//                 imgUrl: 'url',
//                 category: 'Одежда',
//             },
//         ]
//     ],
// ];

// test.each(table)('all products with categories $', (products, categories, expected) => {
//     expect(applyCategories(products, categories)).toStrictEqual(expected);
// });


describe('test applyCategories', () => {
    const productsClothes: Product[] = [
        {
            id: 2,
            name: 'Bershka',
            description: 'T-short',
            price: 14,
            priceSymbol: '₽',
            imgUrl: 'url',
            category: 'Одежда',
        },
        {
            id: 3,
            name: 'H&M',
            description: 'Trousers',
            price: 15,
            priceSymbol: '₽',
            imgUrl: 'url',
            category: 'Одежда',
        },
        {
            id: 4,
            name: 'Bershka',
            description: 'Hat',
            price: 10,
            priceSymbol: '₽',
            imgUrl: 'url',
            category: 'Одежда',
        }
    ];
    const productsElectronic: Product[] = [
        {
            id: 1,
            name: 'MacBook',
            description: 'M2',
            price: 1400,
            priceSymbol: '₽',
            imgUrl: 'url',
            category: 'Электроника',
        }
    ];

    const productsAll: Product[] = [...productsElectronic, ...productsClothes]

    it('several caterogies', () => {
        expect(applyCategories(productsAll, ['Одежда', 'Электроника'])).toStrictEqual(productsAll);
    });

    it('single category', () => {
        expect(applyCategories(productsAll, ['Электроника'])).toStrictEqual(productsElectronic);
    });

    it('empty input', () => {
        expect(applyCategories([], ['Электроника'])).toStrictEqual([]);
    });

    it('empty output', () => {
        expect(applyCategories(productsAll, ['Для дома'])).toStrictEqual([]);
    });
});
