from ..common.constants import PASS_GO_BONUS
from ..common.player import Player
from .board_square import BoardSquare


class GoSquare(BoardSquare):

    def action(self, player: Player):
        player.add_money(PASS_GO_BONUS)
        self.print_message(player)

    def print_message(self, player) -> str:
        print(f'{player.name} lands on go and collects ${PASS_GO_BONUS}')
