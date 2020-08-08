from ..common.constants import Constants
from .board_square import BoardSquare


class Bathroom(BoardSquare):

    def action(self, player):
        player.add_money(-Constants.TAX)
        self.print_message(player)

    def print_message(self, player):
        print(f'{player.name} lands on {self.name}')
