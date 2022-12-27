from typing import Set
import random


def log(f):
    def wrapper(par):
        print('**** {} ****'.format(f.__doc__))
        return f(par)
    return wrapper


class Pizza:
    """
    Содержит и расширяет (по мере поступления новых заказов)
    коллекции рецептов пиццы.
    """
    _sizes = ['L', 'XL']
    _recipes = {'Margherita': {'tomato sauce',
                               'mozzarella',
                               'tomatoes'}}
    _picts = {'Margherita': '🧀'}

    def __init__(self,
                 size: str,
                 name: str,
                 pict: str):
        """
        Обязательно задать:
            - размер
            - название
            - пиктограмму
        пиццы. Рецепт не задается при инициализации,
        а задается отдельно.
        Если задано имя пиццы из имеющегося списка рецептов, то
        в заказ сразу подтягивается имеющийся в базе рецепт и пиктограмма.
        """
        if size not in Pizza._sizes:
            raise ValueError('Bad size of pizza! Take "L" or "XL".')
        if not isinstance(name, str):
            raise TypeError('Bad name of pizza! Must be string type')
        self._size = size
        self._name = name
        if name in Pizza._recipes:
            self._pict = Pizza._picts.get(name)
        else:
            self._pict = pict
            print('Recipe is emty! Please assign it')
        self._recipe = Pizza._recipes.get(name)

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, value: str):
        if value not in Pizza._sizes:
            print('Bad size of pizza! Take "L" or "XL".')
        else:
            self._size = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            print('Bad name of pizza! Must be string type')
        elif value in Pizza._recipes:
            self._recipe = Pizza._recipes.get(value)
            self._pict = Pizza._picts.get(value)
        else:
            self._recipe = None
            self._pict = None
        self._name = value

    @property
    def recipe(self) -> Set[str]:
        return self._recipe

    @recipe.setter
    def recipe(self, value: Set[str]):
        if not isinstance(value, set):
            print('Bad recipe of pizza! Must be list type')
        elif value in Pizza._recipes.values():
            yn = input("The recipe is alredy exists. Change name y/n ?")
            if yn == 'y':
                prec = Pizza._recipes
                self._name = [key for key in prec if prec[key] == value][0]
                self._recipe = Pizza._recipes[self._name]
                self._pict = Pizza._picts[self._name]
        elif self._name in Pizza._recipes:
            print('Can\'t change recipe for the name!')
        else:
            self._recipes[self._name] = value
            self._recipe = value
            self._picts[self._name] = self.pict

    @property
    def pict(self) -> str:
        return self._pict

    @pict.setter
    def pict(self, value: str):
        self._pict = value

    def __eq__(self, other_pizza) -> bool:
        return (self._size == other_pizza._size) and\
               (self._name == other_pizza._name) and\
               (self._recipe == other_pizza._recipe)

    @log
    def bake(pizza):
        """bake"""
        if pizza.recipe == None:
            print('pizza {} hasn\'t recipe!!!'.format(pizza.name))
            print('Shouldn\'t be baked!')
            return
        how_long = random.randint(1, 10)
        print('bake pizza - "{}" in {} minutes'.format(pizza.name, how_long))

    @log
    def delivery(pizza):
        """Delivery pizza"""
        if pizza.recipe == None:
            print('pizza {} hasn\'t recipe!!!'.format(pizza.name))
            print('Shouldn\'t be baked!')
            return
        how_long = random.randint(10, 20)
        print('delivery pizza - "{}" in {} minutes'.format(pizza.name,
                                                           how_long))


if __name__ == '__main__':
    input('          Enter, please\n')
    print('0 *******************************')
    pz1 = Pizza("L", "Noname", '🧀')
    print("pz1.size = {}".format(pz1.size))
    print("pz1.name = {}".format(pz1.name))
    print("pz1.recipe = {}".format(pz1.recipe))
    print("pz1.pict = {}".format(pz1.pict))
    print('1 *******************************')
    input('          Enter, please\n')
    pz1.size = "XL"
    print("pz1.size = {}".format(pz1.size))
    print("pz1.name = {}".format(pz1.name))
    print("pz1.recipe = {}".format(pz1.recipe))
    print("pz1.pict = {}".format(pz1.pict))
    print('2 *******************************')
    input('          Enter, please\n')
    pz1.recipe = {'tomato sauce', 'mozzarella', 'tomatoes'}
    print("pz1.size = {}".format(pz1.size))
    print("pz1.name = {}".format(pz1.name))
    print("pz1.recipe = {}".format(pz1.recipe))
    print("pz1.pict = {}".format(pz1.pict))
    print('3 *******************************')
    input('          Enter, please\n')
    pz2 = Pizza("L", 'Pepperoni', '🍕')
    print("pz2.size = {}".format(pz2.size))
    print("pz2.name = {}".format(pz2.name))
    print("pz2.recipe = {}".format(pz2.recipe))
    print("pz2.pict = {}".format(pz2.pict))
    print('4 *******************************')
    input('          Enter, please\n')
    pz2.recipe = {'tomato sauce', 'mozzarella', 'pepperoni'}
    print("pz2.size = {}".format(pz2.size))
    print("pz2.name = {}".format(pz2.name))
    print("pz2.recipe = {}".format(pz2.recipe))
    print("pz2.pict = {}".format(pz2.pict))
    print('5 *******************************')
    input('          Enter, please\n')
    Pizza.bake(pz1)
    print('6 *******************************')
    input('          Enter, please\n')
    Pizza.delivery(pz1)
    print('7 *******************************')
    input('          Enter, please\n')
    Pizza.bake(pz2)
    print('7 *******************************')
    input('          Enter, please\n')
    print(Pizza._recipes)
    print(Pizza._picts)
