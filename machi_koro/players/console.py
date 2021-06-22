import itertools
from collections import defaultdict

from machi_koro.players.base import Player


class ConsolePlayer(Player):

    def choose_dice_count(self, game):
        self.print_player_town()
        self.print_expected_income(game)
        return int(input('Choose number of dice to roll: '))

    def need_reroll(self, game, dice):
        print('Dice showed ', dice)
        answer = input('Do you need to reroll? (y/N) ')
        return answer.lower().startswith('y')

    def choose_to_build(self, game):
        self.print_player_town()
        self.print_reserve(game)
        print('You have {} coins'.format(self.coins))
        choice = input('What do you wish to build? ').strip()
        while not self.is_eligible_choice(game, choice):
            choice = input('You cannot build this. Choose another: ').strip()
        if choice.lower() == 'nothing' or not choice:
            return choice
        if choice in game.reserve.stacks.keys():
            return game.reserve.stacks[choice]['card']
        return self.town.landmarks[choice]

    def is_eligible_choice(self, game, choice):
        if choice.lower() == 'nothing' or not choice:
            return True
        if choice in game.reserve.stacks.keys():
            card = game.reserve.stacks[choice]['card']
            return self.coins >= card.price
        if choice in self.town.landmarks.keys():
            landmark = self.town.landmarks[choice]
            return self.coins >= landmark.price
        return False

    def print_player_town(self):
        print('    Your town:')
        print('  Landmarks:')
        for landmark in self.town.landmarks.values():
            print('{} {}'.format('[+]' if landmark.built else '[ ]',
                                 landmark.name))
        print('  Establishments:')
        sorted_establishments = sorted(self.town.establishments.values(),
                                       key=lambda estab: estab['card'].spread)
        for record in sorted_establishments:
            print('{} x {}'.format(record['count'], record['card'].name))
        print()

    def print_expected_income(self, game):
        for dice_count in (1, 2):
            print(f'    Expected income for {dice_count} dice:')
            expected_income = self._calculate_expected_income(game, dice_count)
            print('  Total: {:.2f}'.format(expected_income['total']))
            for dice in sorted(expected_income['dice'].keys()):
                income = expected_income['dice'][dice]
                print(f'D = {dice:2}: {income:.2f}')
        print()

    def _calculate_expected_income(self, game, dice_count):
        outcomes = dict()
        for dice in itertools.product(range(1, 7), repeat=dice_count):
            throw_result = sum(dice)
            player_funds = game.activate_cards(throw_result, dry_run=True)
            outcomes[dice] = player_funds[self.name] - self.coins
        total_outcomes = 6 ** dice_count
        expected_income = {
            'dice': defaultdict(list),
            'total': sum(outcomes.values()) / total_outcomes,
        }
        for dice, income in outcomes.items():
            expected_income['dice'][sum(dice)].append(income)
        expected_income['dice'] = {
            key: sum(value) / len(value)
            for key, value in expected_income['dice'].items()
        }
        return expected_income

    @staticmethod
    def print_reserve(game):
        sorted_establishments = sorted(
            game.reserve.stacks.values(),
            key=lambda estab: estab['card'].spread,
        )
        print('  Reserve:')
        for record in sorted_establishments:
            print('{} x {} ({} coins)'.format(
                record['count'],
                record['card'].name,
                record['card'].price))
        print()
