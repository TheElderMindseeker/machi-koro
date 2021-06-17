import pytest

from machi_koro.cards.establishment import Establishment, EstablishmentType, \
    Bakery
from machi_koro.exceptions import IllegalActionError
from machi_koro.reserve import Reserve


def test_put():
    reserve = Reserve()
    assert not reserve.stacks
    reserve.put(Bakery, 2)
    assert Bakery.name in reserve.stacks
    assert reserve.stacks[Bakery.name]['count'] == 2
    reserve.put(Bakery, 4)
    assert reserve.stacks[Bakery.name]['count'] == 6


def test_take():
    reserve = Reserve()
    reserve.put(Bakery, 2)
    assert reserve.stacks[Bakery.name]['count'] == 2
    taken_card = reserve.take(Bakery.name)
    assert (taken_card.spread == Bakery.spread
            and taken_card.price == Bakery.price)
    reserve.take(Bakery.name)
    with pytest.raises(IllegalActionError):
        reserve.take(Bakery.name)
