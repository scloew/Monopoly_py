from ..common import constants
from .board_square import BoardSquare


class Railroad(BoardSquare):

    def action(self, player):
        self.print_message(player)
        return constants.ROLL_AGAIN

    def print_message(self, player):
        print(f'{player.name} lands on {self.name} and rolls again')
