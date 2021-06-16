from machi_koro.cards.establishment import *
from machi_koro.reserve import Reserve
from machi_koro.town import Town


class Game:

    def __init__(self, players):
        self.players = players
        self.reserve = Reserve()

    def setup(self):
        for player in self.players:
            player.town = Town()
            player.town.build(WheatField)
            player.town.build(Bakery)
            player.coins = 3
        for card in self.ESTABLISHMENTS:
            self.reserve.put(card, 6)

    def play(self):
        pass

    ESTABLISHMENTS = (
        WheatField, Ranch, Forest, Mine, AppleOrchard, Bakery, ConvenienceStore,
        CheeseFactory, FurnitureFactory, FnVMarket, Cafe, Restaurant)
