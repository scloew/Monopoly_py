from .board_square import BoardSquare


class Bathroom(BoardSquare):

    def action(self, player):
        self.print_message(player)

    def print_message(self, player):
        print(f'{player.name} lands on {self.name}')
