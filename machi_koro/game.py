from random import randint

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
        winner = None
        while winner is None:
            for player in self.players:
                self.make_turn(player)
                if self.is_winner(player):
                    winner = player
        return winner

    def make_turn(self, player):
        pass

    @staticmethod
    def throw_dice(count):
        dice_sum = 0
        for i in range(count):
            dice_sum += randint(1, 6)
        return dice_sum

    @staticmethod
    def is_winner(player):
        return (
            player.town.train_station.built
            and player.town.shopping_mall.built
            and player.town.amusement_park.built
            and player.town.radio_tower.built
        )

    ESTABLISHMENTS = (
        WheatField, Ranch, Forest, Mine, AppleOrchard, Bakery, ConvenienceStore,
        CheeseFactory, FurnitureFactory, FnVMarket, Cafe, Restaurant)
