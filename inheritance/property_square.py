from ..common.player import Player
from ..common._constants import PROP_PURCHASED
from .board_square import BoardSquare


class PropertySquare(BoardSquare):
    """ class for property square of the board """

    def __init__(self, name, cost):
        super().__init__(name)
        self.cost = cost
        self.owner = None
        self.print_lambda = lambda plyr: print(f'{plyr} purchases {self.name} for {self.cost}')

    def action(self, player: Player):
        if self.owner is None:
            if player.money > self.cost:
                self.owner = player
                self.print_message(player)
                self.print_lambda = lambda plyr: print(f'{plyr} lands on {self.name} {self._owner_msg(plyr)}')
                return PROP_PURCHASED
        self.owner.add_money(self.cost)
        player.add_money(-self.cost)

    def print_message(self, player) -> str:
        return self.print_lambda(player)

    def _owner_msg(self, player):
        return f'and pays {self.cost} to {self.owner}' if self.owner == player else ''
