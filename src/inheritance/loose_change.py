from .board_square import BoardSquare


class LooseChange(BoardSquare):

    def __init__(self, name):
        super().__init__(name)
        self.money_pot = 0

    def action(self, player):
        player.add_money(self.money_pot)
        self.print_message(player)
        self.money_pot = 0
        return None

    def print_message(self, player):
        print(f'{player.name} lands on {self.name} and gains ${self.money_pot}')

    def add_money(self, amt):
        self.money_pot += amt
