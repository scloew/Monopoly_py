from .bathroom import Bathroom
from .chance import ChanceSquare
from .go_square import GoSquare
from .go_to_bathroom import GoToBathRoom
from .loose_change import LooseChange
from .property_square import PropertySquare
from .railroad import Railroad
from .tax_square import TaxSquare


from ..common.constants import TAX


class Board:
    """
    class containing the monopoly squares making up the board
    ordinarily would just return a list but wanted to use classmethod and from_ constructors
    """

    def __init__(self, squares: list[tuple], monopolies: list[tuple]):
        # TODO actually implement monopoly group logic
        types = {
            'bathroom': Bathroom, 'chance': ChanceSquare, 'go': GoSquare,
            'go_to_bathroom': GoToBathRoom, 'loose_change': LooseChange,
            'property': PropertySquare, 'railroad': Railroad, 'tax_square': TaxSquare
        }
        self.squares = [types[class_type](*args_list) for class_type, args_list in squares]

    @classmethod
    def from_default(cls):
        data = []
        data.extend((
                    ('property', 2, ('Magenta 1', 1)), ('property', 3, ('Magenta 2', 1)),
                    ('property', 6, ('Azure 1', 2)),   ('property', 7, ('Azure 2', 2)),
                    ('property', 11, ('Purple 1', 2)), ('property', 15, ('Purple 2', 2)),
                    ('property', 14, ('Orange 1', 3)), ('property', 15, ('Orange 2', 3)),
                    ('property', 18, ('Red 1', 3)),    ('property', 19, ('Red 2', 3)),
                    ('property', 22, ('Yellow 1', 4)), ('property', 22, ('Yellow 2', 4)),
                    ('property', 27, ('Green 1', 4)),  ('property', 27, ('Green 2', 4)),
                    ('property', 30, ('Blue 1', 2)),   ('property', 31, ('Blue 2', 2)),
        ))

        data.extend((
            ('railroad', 5, ('yellow railroad',)), ('railroad', 13, ('green railroad',)),
            ('railroad', 21, ('blue railroad',)), ('railroad', 29, ('red railroad',))
        ))

        data.extend((
            ('tax_square', 8, ('fire works',)), ('tax_square', 24, ('water works',))
        ))

        data.extend((
            ('go', 0, ('Go',)), ('bathroom', 10, ('bathroom',)), ('go_to_bathroom', 4, ('go to bathroom', None, TAX)),
            ('chance', 1, ('chance',)), ('chance', 4, ('chance',)), ('chance', 9, ('chance',)),
            ('chance', 17, ('chance',)), ('chance', 19, ('chance',)), ('chance', 12, ('chance',)),
        ))

        return cls(data)

    @classmethod
    def from_file(cls, file):
        return NotImplemented


if __name__ == '__main__':
    print('hello monopoly?')
    # board = Board.from_default()
    # for i, square in enumerate(board.squares):
    #     print(f'{i}: {square.name}')