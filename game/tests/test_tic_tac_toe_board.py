import pytest
from ultimate_tic_tac_toe.board import TicTacToeBoard
from ultimate_tic_tac_toe.ultimate_tic_tac_toe_errors import (
    InvalidMoveError,
    InvalidStateError,
)

WINNING_POSITIONS = [
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
]


@pytest.fixture
def tic_tac_toe_board_no_winners():

    board = TicTacToeBoard()

    board.make_move(0, (1, 1))
    board.make_move(1, (0, 0))
    board.make_move(0, (2, 2))
    board.make_move(1, (2, 0))
    board.make_move(0, (0, 2))

    return board


def test_tic_tac_toe_board_representation(tic_tac_toe_board_no_winners):

    assert (
        str(tic_tac_toe_board_no_winners)
        == "X |   | O\n--+---+--\n  | O |  \n--+---+--\nX |   | O"
    )


def test_tic_tac_toe_board_all_winning_combinations():

    for player in [0, 1]:
        for case, winning_position in enumerate(WINNING_POSITIONS):
            print(winning_position)
            board = TicTacToeBoard(id=f"test_{case}_player_{player}")
            print(board)
            for position in winning_position:
                board.make_move(player, position)
            assert board.is_winner() == (True, player)


def test_tic_tac_toe_board_no_winner(tic_tac_toe_board_no_winners):
    assert tic_tac_toe_board_no_winners.is_winner() == (False, None)


def test_tic_tac_toe_board_invalid_moves(tic_tac_toe_board_no_winners):

    print(tic_tac_toe_board_no_winners)

    # TODO: Work out how to check custom exceptions, it is not working here.

    with pytest.raises(Exception):
        tic_tac_toe_board_no_winners.make_move(1, (0, 0))

    with pytest.raises(Exception):
        tic_tac_toe_board_no_winners.make_move(2, (0, 1))

    with pytest.raises(Exception):
        tic_tac_toe_board_no_winners.make_move(1, (0, 3))


def test_tic_tac_toe_board_multiple_winners():
    board = TicTacToeBoard()
    board.make_move(0, (0, 0))
    board.make_move(0, (0, 1))
    board.make_move(0, (0, 2))
    board.make_move(1, (2, 0))
    board.make_move(1, (2, 1))
    board.make_move(1, (2, 2))

    # TODO: Work out how to check custom exceptions, it is not working here.

    with pytest.raises(Exception):
        board.is_winner()
