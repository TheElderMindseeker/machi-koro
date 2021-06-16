from collections import namedtuple
from dataclasses import dataclass
from enum import Enum, auto


DiceSpread = namedtuple('Spread', ('min', 'max'))


class EstablishmentType(Enum):
    wheat = auto()
    cow = auto()
    cog = auto()
    store = auto()
    factory = auto()
    fruit = auto()
    coffee = auto()


@dataclass
class Establishment:
    spread: DiceSpread
    name: str
    type: EstablishmentType
    price: int


WheatField = Establishment(
    (1, 1),
    'Wheat Field',
    EstablishmentType.wheat,
    1,
)
Ranch = Establishment(
    (2, 2),
    'Ranch',
    EstablishmentType.cow,
    1,
)
Forest = Establishment(
    (5, 5),
    'Forest',
    EstablishmentType.cog,
    3,
)
Mine = Establishment(
    (9, 9),
    'Mine',
    EstablishmentType.cog,
    6,
)
AppleOrchard = Establishment(
    (10, 10),
    'Apple Orchard',
    EstablishmentType.wheat,
    3,
)

Bakery = Establishment(
    (2, 3),
    'Bakery',
    EstablishmentType.store,
    1,
)
ConvenienceStore = Establishment(
    (4, 4),
    'Convenience Store',
    EstablishmentType.store,
    2,
)
CheeseFactory = Establishment(
    (7, 7),
    'Cheese Factory',
    EstablishmentType.factory,
    5,
)
FurnitureFactory = Establishment(
    (8, 8),
    'Furniture Factory',
    EstablishmentType.factory,
    3,
)
FnVMarket = Establishment(
    (11, 12),
    'Fruit and Vegetable Market',
    EstablishmentType.fruit,
    2,
)

Cafe = Establishment(
    (3, 3),
    'Cafe',
    EstablishmentType.coffee,
    2,
)
Restaurant = Establishment(
    (9, 10),
    'Restaurant',
    EstablishmentType.coffee,
    3,
)
