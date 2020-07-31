from ..common.player import Player
from ..common.constants import TAX
from .board_square import BoardSquare
from .loose_change import LooseChange


class TaxSquare(BoardSquare):

    def __init__(self, name, loose_change: LooseChange):
        super().__init__(name)
        self.loose_change = loose_change

    def action(self, player: Player):
        self.loose_change.add_money(TAX)
        self.print_message(player)

    def print_message(self, player):
        print(f'{player.name} lands on {self.name} and contributes ${TAX} to loose change0')
