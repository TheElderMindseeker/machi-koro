from machi_koro.players.base import Player


class ConsolePlayer(Player):

    def choose_dice_count(self, game):
        self.print_player_town()
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
        landmarks_by_name = {
            landmark.name: landmark for landmark in self.town.landmarks
        }
        return landmarks_by_name[choice]

    def is_eligible_choice(self, game, choice):
        if choice.lower() == 'nothing' or not choice:
            return True
        if choice in game.reserve.stacks.keys():
            card = game.reserve.stacks[choice]['card']
            return self.coins >= card.price
        landmarks_by_name = {
            landmark.name: landmark for landmark in self.town.landmarks
        }
        if choice in landmarks_by_name.keys():
            landmark = landmarks_by_name[choice]
            return self.coins >= landmark.price
        return False

    def print_player_town(self):
        print('    Your town:')
        print('  Landmarks:')
        for landmark in self.town.landmarks:
            print('{} {}'.format(
                '[+]' if landmark.built else '[ ]',
                landmark.name))
        print('  Establishments:')
        sorted_establishments = sorted(self.town.establishments.values(),
                                       key=lambda estab: estab['card'].spread)
        for record in sorted_establishments:
            print('{} x {}'.format(record['count'], record['card'].name))
        print()

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
