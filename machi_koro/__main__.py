import logging

from machi_koro.game import Game
from machi_koro.players import ConsolePlayer

master_logger = logging.getLogger('machi_koro')
master_logger.setLevel(logging.DEBUG)
master_logger.addHandler(logging.StreamHandler())

player = ConsolePlayer('Daniil')
game = Game([player])
game.setup()
player.town.train_station.built = True
winner = game.play()
master_logger.info('Winner is %s', winner.name)
