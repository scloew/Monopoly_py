from .board_square import BoardSquare


class GoToBathRoom(BoardSquare):

    def action(self, player):
        return GoToBathRoom

    def print_message(self, player):
        print(f'{player} moves to bathroom')
