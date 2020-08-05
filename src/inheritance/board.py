from .bathroom import Bathroom
from .chance import ChanceSquare
from .go_square import GoSquare
from .go_to_bathroom import GoToBathRoom
from .loose_change import LooseChange
from .property_square import PropertySquare
from .railroad import Railroad
from .tax_square import TaxSquare

from ..common.constants import Constants
from ..common.monopoly_group import MonopolyGroup


class Board:
    """
    class containing the monopoly squares making up the board
    ordinarily would just return a list but wanted to use class method and from_ constructors
    """

    def __init__(self, squares, monopolies):
        # TODO actually implement monopoly group logic
        self._build_squares(squares)
        self.monopolies = {}
        self._build_monopolies(monopolies)

    def _build_squares(self, squares):
        Constants.BOARD_LENGTH = len(squares)
        squares_tmp = [None for _ in range(Constants.BOARD_LENGTH)]
        self.types = {
            'bathroom': Bathroom, 'chance': ChanceSquare, 'go': GoSquare,
            'go_to_bathroom': GoToBathRoom, 'loose_change': LooseChange,
            'property': PropertySquare, 'railroad': Railroad, 'tax_square': TaxSquare
        }
        lc = LooseChange('Loose Change')
        go_loc = 0
        for class_type, loc, args_list in squares:
            try:
                if class_type == 'tax_square':
                    squares_tmp[loc] = TaxSquare(*args_list, lc)
                    continue
                elif class_type == 'go':
                    squares_tmp[loc] = (GoSquare(*args_list))
                    go_loc = loc
                elif class_type == 'loose_change':
                    squares_tmp[loc] = lc
                    continue
                squares_tmp[loc] = self.types[class_type](*args_list)
            except Exception as e:
                self._handle_board_error(e, class_type, loc, args_list)

        if None in squares_tmp:
            print(f'square {squares_tmp.index(None)} is None; please make sure all indices are valid squares')
            quit()
        self.squares = squares_tmp[go_loc:] + squares_tmp[:go_loc]

    def _build_monopolies(self, monopolies):
        for mn in monopolies:
            temp_monopoly = MonopolyGroup(mn)
            for i in mn:
                self.monopolies[i] = temp_monopoly

    def _handle_board_error(self, error, class_type, loc, args_list):
        new_line = '\n'
        if type(error) == KeyError:
            print(f'Unknown board square {class_type}')
            print(f"supported types:{new_line * 2}{new_line.join(self.types.keys())}")
        elif type(error) == TypeError:
            print(f'invalid argument list {args_list} for type {class_type}')
            print(f'\n {help(self.types[class_type].__init__)}')
        elif type(error) == IndexError:
            print(f'attempted to assign square {class_type} {args_list}')
            print(f'to board location {loc} which is beyond board size of {Constants.BOARD_LENGTH}')
        quit()

    @classmethod
    def from_default(cls):
        data = []
        data.extend((
            ('property', 2, ('Magenta 1', 1)), ('property', 3, ('Magenta 2', 1)),
            ('property', 6, ('Azure 1', 2)),   ('property', 7, ('Azure 2', 2)),
            ('property', 11, ('Purple 1', 2)), ('property', 12, ('Purple 2', 2)),
            ('property', 14, ('Orange 1', 3)), ('property', 15, ('Orange 2', 3)),
            ('property', 18, ('Red 1', 3)),    ('property', 19, ('Red 2', 3)),
            ('property', 22, ('Yellow 1', 4)), ('property', 23, ('Yellow 2', 4)),
            ('property', 27, ('Green 1', 4)),  ('property', 28, ('Green 2', 4)),
            ('property', 30, ('Blue 1', 2)),   ('property', 31, ('Blue 2', 2)),
        ))

        monopolies = ((data[i][1], data[i + 1][1]) for i in range(0, len(data), 2))

        data.extend((
            ('railroad', 5, ('yellow railroad',)), ('railroad', 13, ('green railroad',)),
            ('railroad', 21, ('blue railroad',)), ('railroad', 29, ('red railroad',))
        ))

        data.extend((
            ('loose_change', 16, ('Loose Change',)), ('tax_square', 8, ('fire works',)),
            ('tax_square', 24, ('water works',))
        ))

        data.extend((
            ('go', 0, ('Go',)), ('bathroom', 10, ('bathroom',)), ('go_to_bathroom', 26, ('go to bathroom',)),
            ('chance', 1, ('chance',)), ('chance', 4, ('chance',)), ('chance', 9, ('chance',)),
            ('chance', 17, ('chance',)), ('chance', 20, ('chance',)), ('chance', 25, ('chance',)),
        ))

        return cls(data, monopolies)

    def __str__(self):
        return ' '.join(str(sqr) for sqr in self.squares)

    @classmethod
    def from_file(cls, file):
        return NotImplemented
