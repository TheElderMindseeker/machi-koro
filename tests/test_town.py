import pytest

from machi_koro.cards.establishment import WheatField, Bakery, Cafe, \
    EstablishmentColor
from machi_koro.town import Town


@pytest.fixture
def town():
    town = Town()
    town.build(WheatField)
    town.build(Bakery)
    town.build(Cafe)
    return town


def test_build(town):
    test_town = Town()
    assert not test_town.establishments
    test_town.build(WheatField)
    assert WheatField.name in test_town.establishments
    establishment = test_town.establishments[WheatField.name]
    assert establishment['count'] == 1
    test_town.build(WheatField)
    assert establishment['count'] == 2


def test_get_activated_cards(town):
    red_cards = town.get_activated_cards(EstablishmentColor.red,
                                         Cafe.spread.min)
    assert Cafe.name in red_cards.keys()
    assert WheatField.name not in red_cards.keys()
    blue_cards = town.get_activated_cards(EstablishmentColor.blue,
                                          WheatField.spread.min)
    assert WheatField.name in blue_cards.keys()
    assert Bakery.name not in blue_cards.keys()
    green_cards = town.get_activated_cards(EstablishmentColor.green,
                                           Bakery.spread.min)
    assert Bakery.name in green_cards.keys()
    assert Cafe.name not in green_cards.keys()
