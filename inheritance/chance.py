from random import choice

from ..common.player import Player
from ..common.constants import CHANCE_ADD_MONEY, CHANCE_MOVE, BOARD_LENGTH
from .board_square import BoardSquare


class ChanceSquare(BoardSquare):

    def __init__(self, name):
        super().__init__(self)
        self.print_lambda = None

    def action(self, player: Player):
        action = choice(CHANCE_MOVE, CHANCE_ADD_MONEY)
        if action == CHANCE_ADD_MONEY:
            money = choice(range(-5, 6))
            player.add_money(money)
            self.print_lambda =  f'chance contributes ${money} to {player.name}'
        else:
            new_loc = choice(range(BOARD_LENGTH))
            self.print_lambda = f'Chance moves {player.name} to square {new_loc}'
        self.print_message(player)

    def print_message(self, player) -> str:
        self.print_lambda(player)
