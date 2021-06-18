import logging
from copy import copy
from random import randint

from machi_koro.cards.establishment import *
from machi_koro.cards.landmark import Landmark
from machi_koro.exceptions import IllegalActionError
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
                self.active_player = player
                self.logger.info("It's %s's turn", self.active_player.name)
                self.make_turn()
                if self.is_winner(player):
                    winner = player
                    self.logger.info('%s is the winner!', winner.name)
        return winner

    def make_turn(self, bonus=False):
        dice_count = 1
        if self.active_player.town.train_station.built:
            dice_count = self.active_player.choose_dice_count(self)
            if dice_count not in (1, 2):
                raise IllegalActionError('Player tried to throw %d dice',
                                         dice_count)
        dice = self.throw_dice(dice_count)
        if self.active_player.town.radio_tower.built:
            if self.active_player.need_reroll(self, dice):
                dice = self.throw_dice(dice_count)
        self.activate_cards(sum(dice))
        card_to_build = self.active_player.choose_to_build(self)
        if isinstance(card_to_build, Establishment):
            if card_to_build.price > self.active_player.coins:
                raise IllegalActionError('Player %s has insufficient funds',
                                         self.active_player.name)
            taken_card = self.reserve.take(card_to_build.name)
            self.active_player.coins -= card_to_build.price
            self.active_player.town.build(taken_card)
            self.logger.info('%s builds %s', self.active_player.name,
                             taken_card.name)
        elif isinstance(card_to_build, Landmark):
            if card_to_build.price > self.active_player.coins:
                raise IllegalActionError('Player %s has insufficient funds',
                                         self.active_player.name)
            self.active_player.coins -= card_to_build.price
            card_to_build.built = True
            self.logger.info('%s builds %s', self.active_player.name,
                             card_to_build.name)
        else:
            self.logger.info('%s chooses to build nothing',
                             self.active_player.name)
        if (self.active_player.town.amusement_park.built
                and not bonus and dice_count == 2 and dice[0] == dice[1]):
            self.logger.info('%s got a double and makes a bonus turn',
                             self.active_player.name)
            self.make_turn(bonus=True)

    @staticmethod
    def is_winner(player):
        return (
            player.town.train_station.built
            and player.town.shopping_mall.built
            and player.town.amusement_park.built
            and player.town.radio_tower.built
        )

    def throw_dice(self, count):
        dice = tuple(randint(1, 6) for _ in range(count))
        self.logger.info('%d dice were thrown: %s', count, dice)
        return dice

    def activate_cards(self, throw_result, dry_run=False):
        self.dry_run = dry_run
        self.player_funds = {
            player.name: player.coins for player in self.players
        }
        active_index = self.players.index(self.active_player)
        reverse_order = reversed(self.players[active_index + 1:]
                                 + self.players[:active_index])
        for player in reverse_order:
            self._activate_red_cards(player, throw_result)
        for player in self.players:
            self._activate_blue_cards(player, throw_result)
        self._activate_green_cards(throw_result)
        if not self.dry_run:
            for player in self.players:
                player.coins = self.player_funds[player.name]
        return copy(self.player_funds)

    def _activate_red_cards(self, player, throw_result):
        activated_card_names = player.town.get_activated_card_names(
            EstablishmentColor.red, throw_result)
        for card_name in activated_card_names:
            income = player.town.calculate_income(card_name)
            coins_stolen = min(
                income, self.player_funds[self.active_player.name])
            self.player_funds[self.active_player.name] -= coins_stolen
            self.player_funds[player.name] += coins_stolen
            if not self.dry_run:
                self.logger.info(
                    '%s steals %d coins from %s using %s',
                    player.name,
                    coins_stolen,
                    self.active_player.name,
                    card_name,
                )

    def _activate_blue_cards(self, player, throw_result):
        activated_card_names = player.town.get_activated_card_names(
            EstablishmentColor.blue, throw_result)
        for card_name in activated_card_names:
            income = player.town.calculate_income(card_name)
            self.player_funds[player.name] += income
            if not self.dry_run:
                self.logger.info(
                    '%s makes %d coins using %s',
                    player.name,
                    income,
                    card_name,
                )

    def _activate_green_cards(self, throw_result):
        activated_card_names = self.active_player.town.get_activated_card_names(
            EstablishmentColor.green, throw_result)
        for card_name in activated_card_names:
            income = self.active_player.town.calculate_income(card_name)
            self.player_funds[self.active_player.name] += income
            if not self.dry_run:
                self.logger.info(
                    '%s makes %d coins using %s',
                    self.active_player.name,
                    income,
                    card_name,
                )

    ESTABLISHMENTS = (
        WheatField, Ranch, Forest, Mine, AppleOrchard, Bakery, ConvenienceStore,
        CheeseFactory, FurnitureFactory, FnVMarket, Cafe, Restaurant)

    logger = logging.getLogger(__name__)
