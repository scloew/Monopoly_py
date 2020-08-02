#from ..common.constants import ROLL_AGAIN
from .board_square import BoardSquare

ROLL_AGAIN = 4

class Railroad(BoardSquare):

    def action(self, player):
        self.print_message(player)
        return ROLL_AGAIN

    def print_message(self, player):
        print(f'{player.name} lands on {self.name} and rolls again')
