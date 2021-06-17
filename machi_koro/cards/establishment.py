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


class EstablishmentColor(Enum):
    blue = auto()
    green = auto()
    red = auto()


CONSTANT_MULTIPLIER = 'constant'


@dataclass
class Establishment:
    spread: DiceSpread
    name: str
    color: EstablishmentColor
    type: EstablishmentType
    price: int
    income: int
    multiplier: str


WheatField = Establishment(
    DiceSpread(1, 1),
    'Wheat Field',
    EstablishmentColor.blue,
    EstablishmentType.wheat,
    1,
    1,
    CONSTANT_MULTIPLIER,
)
Ranch = Establishment(
    DiceSpread(2, 2),
    'Ranch',
    EstablishmentColor.blue,
    EstablishmentType.cow,
    1,
    1,
    CONSTANT_MULTIPLIER,
)
Forest = Establishment(
    DiceSpread(5, 5),
    'Forest',
    EstablishmentColor.blue,
    EstablishmentType.cog,
    3,
    1,
    CONSTANT_MULTIPLIER,
)
Mine = Establishment(
    DiceSpread(9, 9),
    'Mine',
    EstablishmentColor.blue,
    EstablishmentType.cog,
    6,
    5,
    CONSTANT_MULTIPLIER,
)
AppleOrchard = Establishment(
    DiceSpread(10, 10),
    'Apple Orchard',
    EstablishmentColor.blue,
    EstablishmentType.wheat,
    3,
    3,
    CONSTANT_MULTIPLIER,
)

Bakery = Establishment(
    DiceSpread(2, 3),
    'Bakery',
    EstablishmentColor.green,
    EstablishmentType.store,
    1,
    1,
    CONSTANT_MULTIPLIER,
)
ConvenienceStore = Establishment(
    DiceSpread(4, 4),
    'Convenience Store',
    EstablishmentColor.green,
    EstablishmentType.store,
    2,
    3,
    CONSTANT_MULTIPLIER,
)
CheeseFactory = Establishment(
    DiceSpread(7, 7),
    'Cheese Factory',
    EstablishmentColor.green,
    EstablishmentType.factory,
    5,
    3,
    f'type:{EstablishmentType.cow.name}',
)
FurnitureFactory = Establishment(
    DiceSpread(8, 8),
    'Furniture Factory',
    EstablishmentColor.green,
    EstablishmentType.factory,
    3,
    3,
    f'type:{EstablishmentType.cog.name}',
)
FnVMarket = Establishment(
    DiceSpread(11, 12),
    'Fruit and Vegetable Market',
    EstablishmentColor.green,
    EstablishmentType.fruit,
    2,
    2,
    f'type:{EstablishmentType.wheat.name}',
)

Cafe = Establishment(
    DiceSpread(3, 3),
    'Cafe',
    EstablishmentColor.red,
    EstablishmentType.coffee,
    2,
    1,
    CONSTANT_MULTIPLIER,
)
Restaurant = Establishment(
    DiceSpread(9, 10),
    'Restaurant',
    EstablishmentColor.red,
    EstablishmentType.coffee,
    3,
    2,
    CONSTANT_MULTIPLIER,
)
