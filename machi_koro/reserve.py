from machi_koro.exceptions import IllegalActionError


class Reserve:

    def __init__(self):
        self.stacks = dict()

    def put(self, card, count):
        if card.name in self.stacks.keys():
            self.stacks[card.name]['count'] += count
        else:
            self.stacks[card.name] = {'card': card, 'count': count}

    def take(self, card_name):
        try:
            card = self.stacks[card_name]['card']
            self.stacks[card_name]['count'] -= 1
            if self.stacks[card_name]['count'] <= 0:
                del self.stacks[card_name]
            return card
        except KeyError as exc:
            raise IllegalActionError(
                'No more %s cards in reserve', card_name) from exc
