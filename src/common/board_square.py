class BoardSquare:
    """
    base (abstract) class for a monopoly square in the board
    use requires implementation of action and print_message
    """

    def __init__(self, name):
        self.name = name

    def action(self, player):
        return NotImplemented

    def print_message(self, player):
        return NotImplemented

    def __str__(self):
        return self.name
