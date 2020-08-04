from src.inheritance.board import Board

if __name__ == '__main__':
    b = Board.from_default()
    for i, s in enumerate(b.squares):
        print(i, s)

    print(f'monopolies are {b.monopolies}')

    print(str(b.squares[3]))
    #
    # for key, val in b.monopolies.items():
    #     print(val)
