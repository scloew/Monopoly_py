from src.inheritance.board import Board

if __name__ == '__main__':
    b = Board.from_default()
    for i, s in enumerate(b.squares):
        print(i, s)
