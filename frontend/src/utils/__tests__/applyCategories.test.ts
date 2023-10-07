import { Product } from '../../types';
import { applyCategories } from '../applyCategories';

describe('test applyCategories', () => {
    const productElectronic: Product[] = [
        {
            id: 1,
            name: 'test1',
            description: 'test1',
            price: 1,
            priceSymbol: '$',
            category: 'Электроника',
        },
        {
            id: 2,
            name: 'test2',
            description: 'test2',
            price: 2,
            priceSymbol: '$',
            category: 'Электроника',
        },
    ];
    const productWear: Product[] = [
        {
            id: 3,
                name: 'test3',
            description: 'test3',
            price: 3,
            priceSymbol: '$',
            category: 'Одежда',
        },
    ]

    const productAll: Product[] = [...productElectronic, ...productWear]

    it('all products for empty categories', () => {
        expect(applyCategories(productAll, [])).toEqual(productAll);
    });

    it('filter electronic category', () => {
        expect(applyCategories(productAll, ['Электроника'])).toEqual(productElectronic);
    });

    it('filter wear category', () => {
        expect(applyCategories(productAll, ['Одежда'])).toEqual(productWear);
    });
});