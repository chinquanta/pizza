from pizza import Pizza
import pytest


def test_init():
    pizza_exists = Pizza('XL', 'Margherita', '🧀')
    assert pizza_exists.size == 'XL'
    assert pizza_exists.name == 'Margherita'
    assert pizza_exists.recipe == {'mozzarella', 'tomatoes', 'tomato sauce'}
    assert pizza_exists.pict == '🧀'
    pizza_exists = Pizza('L', 'Pepperoni', '🍕')
    assert pizza_exists.size == 'L'
    assert pizza_exists.name == 'Pepperoni'
    assert pizza_exists.recipe is None
    assert pizza_exists.pict == '🍕'
    assert Pizza._recipes.get('Pepperoni') is None
    assert Pizza._picts.get('Pepperoni') is None
    pizza_exists.recipe = {'mozzarella', 'pepperoni', 'tomato sauce'}
    assert pizza_exists.recipe == {'mozzarella', 'pepperoni', 'tomato sauce'}
    assert Pizza._recipes.get('Pepperoni') == {'mozzarella', 'pepperoni',
                                               'tomato sauce'}
    assert Pizza._picts.get('Pepperoni') == '🍕'


@pytest.mark.parametrize('s,exp',
                         [(('XXL', 'Margherita', '🧀'),
                           pytest.raises(ValueError)),
                          ((100, 'Margherita', '🧀'),
                           pytest.raises(ValueError))])
def test_raises(s, exp):
    with exp:
        assert Pizza(*s) == exp


if __name__ == '__main__':
    pass
