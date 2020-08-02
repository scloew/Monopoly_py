from random import choice

from ..common.constants import Constants
from .board_square import BoardSquare


class ChanceSquare(BoardSquare):

    def __init__(self, name):
        super().__init__(name)
        self.print_msg = None

    def action(self, player):
        action = choice(Constants.CHANCE_MOVE, Constants.CHANCE_ADD_MONEY)
        if action == Constants.CHANCE_ADD_MONEY:
            money = choice(range(-5, 6))
            player.add_money(money)
            self.print_msg = f'chance contributes ${money} to {player.name}'
        else:
            new_loc = choice(range(Constants.board_length))
            self.print_msg = f'Chance moves {player.name} to square {new_loc}'
        self.print_message(player)

    def print_message(self, player):
        self.print_msg(player)
