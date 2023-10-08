import {useProducts} from '../../hooks';
import {Category, Product} from '../../types';
import {applyCategories} from '../applyCategories';

describe('tests for applyCategories function', () => {
    const allCategories: Category[] = ['Одежда', 'Для дома', 'Электроника'];
    const allPoruducts: Product[] = [
        {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/iphone.png',
        },
        {
            id: 2,
            name: 'Костюм гуся',
            description: 'Запускаем гуся, работяги',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
        {
            id: 3,
            name: 'Настольная лампа',
            description: 'Говорят, что ее использовали в pixar',
            price: 699,
            category: 'Для дома',
            imgUrl: '/lamp.png',
        },
        {
            id: 4,
            name: 'Принтер',
            description: 'Незаменимая вещь для студента',
            price: 7000,
            category: 'Электроника',
        },
    ];

    it('should return products by category', () => {
        expect(applyCategories(allPoruducts, allCategories)).toEqual(allPoruducts);
        expect(applyCategories(allPoruducts, [allCategories[1]])).toEqual([allPoruducts[2]]);
        expect(applyCategories(allPoruducts, allCategories.slice(1, 3))).toEqual([allPoruducts[0], ...allPoruducts.slice(2)]);
        expect(applyCategories(allPoruducts, [])).toEqual(allPoruducts);
    });
});
