from src.common.constants import Constants
from src.common.board_square import BoardSquare


class GoSquare(BoardSquare):

    def action(self, player):
        player.add_money(Constants.PASS_GO_BONUS)
        self.print_message(player)

    def print_message(self, player):
        print(f'{player} lands on go and collects ${Constants.PASS_GO_BONUS}')
