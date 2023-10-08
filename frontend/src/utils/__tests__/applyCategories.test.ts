import {useProducts} from '../../hooks';
import {applyCategories} from '../applyCategories';
import {Category, Product} from '../../types';

describe('test apply categories function', () => {
  const products: Product[] = [
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
  ]

  it('should return list of product containing all categoties if categories list is empty', () => {
    const selectedCategories: Category[] = [];

    expect(applyCategories(products, selectedCategories)).toEqual(products);
  });

  it('should return list of product containing all categoties if categories list is full', () => {
    const selectedCategories: Category[] = [
      'Электроника',
      'Для дома',
      'Одежда',
    ];

    expect(applyCategories(products, selectedCategories)).toEqual(products);
  });

  it('should return list of product containing selected categoties', () => {
    const selectedCategories: Category[] = [
      'Электроника',
      'Для дома',
    ];
    const products = useProducts();

    expect(applyCategories(products, selectedCategories)).toEqual([
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
    ]);
  });
});
