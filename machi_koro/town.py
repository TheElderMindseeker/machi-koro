from machi_koro.cards.establishment import EstablishmentType
from machi_koro.cards.landmark import Landmark


class Town:

    def __init__(self):
        self.train_station = Landmark('Train Station', 4)
        self.shopping_mall = Landmark('Shopping Mall', 10)
        self.amusement_park = Landmark('Amusement Park', 16)
        self.radio_tower = Landmark('Radio Tower', 22)
        self.establishments = dict()

    def build(self, establishment):
        estab_name = establishment.name
        if estab_name in self.establishments.keys():
            self.establishments[estab_name]['count'] += 1
        else:
            self.establishments[estab_name] = {
                'card': establishment,
                'count': 1,
            }

    def get_activated_card_names(self, color, throw_result):
        cards = list()
        for record in self.establishments.values():
            card = record['card']
            if (card.color == color
                    and card.spread.min <= throw_result <= card.spread.max):
                cards.append(record['card'].name)
        return cards

    def calculate_income(self, estab_name):
        card = self.establishments[estab_name]['card']
        count = self.establishments[estab_name]['count']
        effective_income = card.income
        if self.shopping_mall.built and card.type in self.SHOPPING_MALL_TYPES:
            effective_income += 1
        if card.multiplier.startswith('type:'):
            estab_type = EstablishmentType[card.multiplier.split(':')[1]]
            total_estab_count = sum(
                record['count'] for record in self.establishments.values()
                if record['card'].type == estab_type
            )
            effective_income *= total_estab_count
        return count * effective_income

    @property
    def landmarks(self):
        return (
            self.train_station,
            self.shopping_mall,
            self.amusement_park,
            self.radio_tower,
        )

    SHOPPING_MALL_TYPES = (EstablishmentType.store, EstablishmentType.coffee)
