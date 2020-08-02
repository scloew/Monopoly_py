from .bathroom import Bathroom
from .chance import ChanceSquare
from .go_square import GoSquare
from .go_to_bathroom import GoToBathRoom
from .loose_change import LooseChange
from .property_square import PropertySquare
from .railroad import Railroad
from .tax_square import TaxSquare

from ..common.constants import Constants

class Board:
    """
    class containing the monopoly squares making up the board
    ordinarily would just return a list but wanted to use classmethod and from_ constructors
    """

    def __init__(self, squares, monopolies):
        # TODO actually implement monopoly group logic
        types = {
            'bathroom': Bathroom, 'chance': ChanceSquare, 'go': GoSquare,
            'go_to_bathroom': GoToBathRoom, 'loose_change': LooseChange,
            'property': PropertySquare, 'railroad': Railroad, 'tax_square': TaxSquare
        }
        lc = LooseChange('Loose Change')
        Constants.BOARD_LENGTH = len(squares)
        self.squares = [None for _ in range(Constants.BOARD_LENGTH)]
        new_line = '\n'
        for class_type, loc, args_list in squares:
            try:
                if class_type == 'tax_square':
                    self.squares[loc] = TaxSquare(*args_list, lc)
                    continue
                elif class_type == 'loose_change':
                    self.squares.append(lc)
                    continue
                self.squares[loc] = types[class_type](*args_list)
            except KeyError:
                print(f'Unknown board square {class_type}')
                print(f"supported types:{new_line*2}{new_line.join(types.keys())}")
                quit()
            except TypeError:
                print(f'invalid argument list {args_list} for type {class_type}')
                print(f'expected:\n {help(types[class_type].__init__)}')
                quit()
            except IndexError:
                print(f'attempted to assign square {class_type} {args_list}')
                print(f'to board location {loc} which is beyond board size of {Constants.BOARD_LENGTH}')
                quit()

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
            ('loose_change', 16, ('Loose Change',)), ('tax_square', 8, ('fire works',)),
            ('tax_square', 24, ('water works',))
        ))

        data.extend((
            ('go', 0, ('Go',)), ('bathroom', 10, ('bathroom',)), ('go_to_bathroom', 4, ('go to bathroom',)),
            ('chance', 1, ('chance',)), ('chance', 4, ('chance',)), ('chance', 9, ('chance',)),
            ('chance', 17, ('chance',)), ('chance', 19, ('chance',)), ('chance', 12, ('chance',)),
        ))

        return cls(data, [])

    @classmethod
    def from_file(cls, file):
        return NotImplemented
