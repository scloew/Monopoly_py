from src.common.constants import Constants
from src.common.board_square import BoardSquare


class TaxSquare(BoardSquare):

    def __init__(self, name, loose_change):
        super().__init__(name)
        self.loose_change = loose_change

    def action(self, player):
        player.add_money(-Constants.TAX)
        self.loose_change.add_money(Constants.TAX)
        self.print_message(player)

    def print_message(self, player):
        print(f'{player.name} lands on {self.name} and contributes ${Constants.TAX} to loose change')
