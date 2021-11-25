class BoardSquare:
    """
    base (abstract) class for a monopoly square in the board
    use requires implementation of action and print_message
    """

    def __init__(self, name, **kwargs):
        self.name = name

    def action(self, player):
        raise NotImplementedError

    def print_message(self, player):
        raise NotImplementedError

    def __str__(self):
        return self.name
