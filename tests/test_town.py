from machi_koro.town import Town
from machi_koro.cards.establishment import Establishment, EstablishmentType


def test_build():
    test_town = Town()
    assert not test_town.establishments
    test_estab = Establishment((1, 1), 'Test', EstablishmentType.cog, 1)
    test_town.build(test_estab)
    assert test_estab.name in test_town.establishments
    establishment = test_town.establishments[test_estab.name]
    assert establishment['count'] == 1
    test_town.build(test_estab)
    assert establishment['count'] == 2
