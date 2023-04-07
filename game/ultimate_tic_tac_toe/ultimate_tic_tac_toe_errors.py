class UltimateTicTacToeGameError(Exception):
    """
    Named error for the ultimate Tic Tac Toe game.
    """


class TicTacToeBoardError(UltimateTicTacToeGameError):
    """
    Named error for the Tic Tac Toe board.
    """


class InvalidMoveError(TicTacToeBoardError):
    """
    Named error for invalid moves.
    """


class InvalidStateError(TicTacToeBoardError):
    """
    Named error for invalid states.
    """
