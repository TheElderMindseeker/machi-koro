import logging
from random import sample

from machi_koro.game import Game
from machi_koro.players import BuildOrderPlayer

master_logger = logging.getLogger('machi_koro')
master_logger.setLevel(logging.WARNING)
master_logger.addHandler(logging.StreamHandler())

ranch_build_order = (
    'E:Ranch',
    'E:Ranch',
    'E:Ranch',
    'L:Train Station',
    'E:Cheese Factory',
    'E:Cheese Factory',
    'E:Cheese Factory',
    'L:Amusement Park',
    'L:Radio Tower',
    'L:Shopping Mall',
)

forest_build_order = (
    'E:Wheat Field',
    'E:Wheat Field',
    'E:Forest',
    'E:Forest',
    'E:Forest',
    'L:Train Station',
    'E:Furniture Factory',
    'E:Furniture Factory',
    'E:Furniture Factory',
    'L:Shopping Mall',
    'L:Amusement Park',
    'L:Radio Tower',
)

convenience_build_order = (
    'E:Bakery',
    'E:Convenience Store',
    'E:Convenience Store',
    'E:Convenience Store',
    'L:Shopping Mall',
    'E:Convenience Store',
    'L:Train Station',
    # 'E:Restaurant',
    # 'E:Restaurant',
    'L:Amusement Park',
    'L:Radio Tower',
)

players = (
    BuildOrderPlayer('Dr. Jekyll', ranch_build_order),
    BuildOrderPlayer('Mr. Hyde', ranch_build_order),
    # BuildOrderPlayer('Robin Hood', forest_build_order),
    BuildOrderPlayer('Daniil', convenience_build_order),
)
win_stats = {player.name: 0 for player in players}

for i in range(1000):
    players = (
        BuildOrderPlayer('Dr. Jekyll', ranch_build_order),
        BuildOrderPlayer('Mr. Hyde', ranch_build_order),
        # BuildOrderPlayer('Robin Hood', forest_build_order),
        BuildOrderPlayer('Daniil', convenience_build_order),
    )
    game = Game(sample(players, k=len(players)))
    game.setup()
    winner = game.play()
    win_stats[winner.name] += 1

print(win_stats)
