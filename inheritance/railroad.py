from ..common.player import Player
from ..common.constants import ROLL_AGAIN
from .board_square import BoardSquare


class Railroad(BoardSquare):

    def action(self, player: Player):
        self.print_message(player)
        return ROLL_AGAIN

    def print_message(self, player):
        print(f'{player.name} lands on {self.name} and rolls again')
