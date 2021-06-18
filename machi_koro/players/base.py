from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self, name):
        self.name = name
        self.town = None
        self.coins = 0

    def __eq__(self, other):
        return self.name == other.name

    @abstractmethod
    def choose_dice_count(self, game):
        raise NotImplementedError

    @abstractmethod
    def need_reroll(self, game, dice):
        raise NotImplementedError

    @abstractmethod
    def choose_to_build(self, game):
        raise NotImplementedError
