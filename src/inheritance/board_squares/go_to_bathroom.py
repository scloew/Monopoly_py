from src.common.board_square import BoardSquare
from ...common.constants import Constants


class GoToBathRoom(BoardSquare):

    def action(self, player):
        return Constants.GO_TO_BATHROOM

    def print_message(self, player):
        print(f'{player} moves to bathroom')
