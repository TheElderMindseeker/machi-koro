import pytest

from machi_koro.cards.establishment import *
from machi_koro.town import Town


@pytest.fixture
def town():
    town = Town()
    town.build(WheatField)
    town.build(Bakery)
    town.build(Cafe)
    for i in range(3):
        town.build(Forest)
    town.build(FurnitureFactory)
    return town


def test_build():
    test_town = Town()
    assert not test_town.establishments
    test_town.build(WheatField)
    assert WheatField.name in test_town.establishments
    establishment = test_town.establishments[WheatField.name]
    assert establishment['count'] == 1
    test_town.build(WheatField)
    assert establishment['count'] == 2


def test_get_activated_cards(town):
    red_cards = town.get_activated_card_names(EstablishmentColor.red,
                                              Cafe.spread.min)
    assert Cafe.name in red_cards
    assert WheatField.name not in red_cards
    blue_cards = town.get_activated_card_names(EstablishmentColor.blue,
                                               WheatField.spread.min)
    assert WheatField.name in blue_cards
    assert Bakery.name not in blue_cards
    green_cards = town.get_activated_card_names(EstablishmentColor.green,
                                                Bakery.spread.min)
    assert Bakery.name in green_cards
    assert Cafe.name not in green_cards


def test_calculate_income(town):
    wheat_field_income = town.calculate_income(WheatField.name)
    assert wheat_field_income == 1
    forest_income = town.calculate_income(Forest.name)
    assert forest_income == 3
    with pytest.raises(KeyError):
        town.calculate_income(Restaurant.name)
    shopping_mall_state = town.shopping_mall.built
    town.shopping_mall.built = False
    cafe_income = town.calculate_income(Cafe.name)
    assert cafe_income == 1
    town.shopping_mall.built = True
    cafe_improved_income = town.calculate_income(Cafe.name)
    assert cafe_improved_income == 2
    town.shopping_mall.built = shopping_mall_state
    furniture_income = town.calculate_income(FurnitureFactory.name)
    assert furniture_income == 9
