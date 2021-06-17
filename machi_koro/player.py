from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self, name):
        self.name = name
        self.town = None
        self.coins = 0

    def __eq__(self, other):
        return self.name == other.name

    @abstractmethod
    def choose_dice(self, game):
        raise NotImplementedError
