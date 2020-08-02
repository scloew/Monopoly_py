#from ..common.constants import PROP_PURCHASED
from .board_square import BoardSquare

PROP_PURCHASED = 1

class PropertySquare(BoardSquare):
    """ class for property square of the board """

    def __init__(self, name, cost):
        super().__init__(name)
        self.cost = cost
        self.owner = None
        self.print_lambda = lambda plyr: print(f'{plyr} purchases {self.name} for {self.cost}')

    def action(self, player):
        if self.owner is None:
            if player.money > self.cost:
                self.owner = player
                self.print_message(player)
                self.print_lambda = lambda plyr: f'and pays {self.cost} to {self.owner}' if self.owner == player else ''
                return PROP_PURCHASED
        self.print_message(player)
        self.owner.add_money(self.cost)
        player.add_money(-self.cost)
        return None

    def print_message(self, player) -> str:
        return self.print_lambda(player)

    def __str__(self):
        return f'name={self.name} owner={self.owner}'
