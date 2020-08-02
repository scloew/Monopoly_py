from ..common.constants import Constants
from .board_square import BoardSquare


class TaxSquare(BoardSquare):

    def __init__(self, name, loose_change):
        super().__init__(name)
        self.loose_change = loose_change

    def action(self, player):
        self.loose_change.add_money(Constants.TAX)
        self.print_message(player)

    def print_message(self, player):
        print(f'{player.name} lands on {self.name} and contributes ${TAX} to loose change0')
