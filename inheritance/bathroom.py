from ..common.player import Player
from .board_square import BoardSquare


class Bathroom(BoardSquare):

    def action(self, player: Player):
        self.print_message(player)

    def print_message(self, player) -> str:
        print(f'{player.name} lands on {self.name}')
