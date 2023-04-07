from board import TicTacToeBoard

if __name__ == "__main__":
    board = TicTacToeBoard()
    board.make_move(0, (0, 0))
    board.make_move(1, (0, 1))
    board.make_move(0, (0, 2))
    board.make_move(1, (1, 1))
    board.make_move(0, (2, 2))
    board.make_move(1, (2, 0))
    print(board)
    print(board.is_winner())
