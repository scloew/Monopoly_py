from ..common.player import Player
from .property_square import PropertySquare


class GoToBathRoom(PropertySquare):

    def action(self, player: Player):
        return GoToBathRoom

    def print_message(self, player):
        print(f'{player} moves to bathroom')
