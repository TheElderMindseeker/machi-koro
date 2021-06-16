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
