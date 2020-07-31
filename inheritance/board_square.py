from ..common.player import Player


class BoardSquare:
    """
    base (abstract) class for a monopoly square in the board
    use requires implementation of action and print_message
    """

    def __init__(self, name: str):
        self.name = name

    def action(self, player: Player):
        return NotImplemented

    def print_message(self, player) -> str:
        return NotImplemented
