import itertools
import logging

from machi_koro.exceptions import EmptyBuildOrderError
from machi_koro.players.base import Player


class BuildOrderPlayer(Player):

    def __init__(self, name, build_order):
        super().__init__(name)
        self.build_order = list(build_order)

    def choose_dice_count(self, game):
        expected_incomes = {
            count: self._calculate_expected_income(game, count)
            for count in (1, 2)
        }
        sorted_incomes = sorted(expected_incomes.items(),
                                key=lambda item: item[1])
        self.logger.debug(sorted_incomes)
        return sorted_incomes[-1][0]

    def need_reroll(self, game, dice):
        return False

    def choose_to_build(self, game):
        self.logger.info('%s has %d coins', self.name, self.coins)
        build_choice = None
        while build_choice is None:
            if not self.build_order:
                raise EmptyBuildOrderError
            card_type, card_name = self.build_order[0].split(':')
            if card_type == 'E':  # Establishment
                try:
                    card = game.reserve.stacks[card_name]['card']
                    if card.price > self.coins:
                        return 'nothing'
                    self.build_order.pop(0)
                    return card
                except KeyError:
                    self.build_order.pop(0)
            else:
                landmark = self.town.landmarks[card_name]
                if landmark.price > self.coins:
                    return 'nothing'
                self.build_order.pop(0)
                return landmark

    def _calculate_expected_income(self, game, dice_count):
        expected_income = .0
        for dice in itertools.product(range(1, 7), repeat=dice_count):
            throw_result = sum(dice)
            player_funds = game.activate_cards(throw_result, dry_run=True)
            expected_income += player_funds[self.name] - self.coins
        total_outcomes = 6 ** dice_count
        return expected_income / total_outcomes

    logger = logging.getLogger(__name__)
