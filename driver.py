from inheritance.board import Board

if __name__ == '__main__':
    b = Board.from_default()
    for i in b.squares:
        print(i)
