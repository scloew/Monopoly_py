#from ..common.constants import PASS_GO_BONUS
from .board_square import BoardSquare

PASS_GO_BONUS = 3

class GoSquare(BoardSquare):

    def action(self, player):
        player.add_money(PASS_GO_BONUS)
        self.print_message(player)

    def print_message(self, player):
        print(f'{player.name} lands on go and collects ${PASS_GO_BONUS}')
