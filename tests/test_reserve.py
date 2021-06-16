import pytest

from machi_koro.cards.establishment import Establishment, EstablishmentType
from machi_koro.exceptions import IllegalActionError
from machi_koro.reserve import Reserve


def test_put():
    reserve = Reserve()
    assert not reserve.stacks
    card = Establishment((1, 1), 'Test', EstablishmentType.cog, 1)
    reserve.put(card, 2)
    assert card.name in reserve.stacks
    assert reserve.stacks[card.name]['count'] == 2
    reserve.put(card, 4)
    assert reserve.stacks[card.name]['count'] == 6


def test_take():
    reserve = Reserve()
    card = Establishment((1, 1), 'Test', EstablishmentType.cog, 1)
    reserve.put(card, 2)
    assert reserve.stacks[card.name]['count'] == 2
    taken_card = reserve.take(card.name)
    assert taken_card.spread == card.spread and taken_card.price == card.price
    reserve.take(card.name)
    with pytest.raises(IllegalActionError):
        reserve.take(card.name)
