from typing import Tuple, Union, List
import logging

from ultimate_tic_tac_toe_errors import (
    InvalidMoveError,
    InvalidStateError,
)


class TicTacToeBoard:

    _markers: dict = {0: "O", 1: "X"}
    _logger = logging.getLogger(__name__)

    def __init__(self, id: str = "main"):
        self._id = id
        self._board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def make_move(self, player: int, move: Tuple[int, int]):
        """
        This makes a move on the board.

        Args:
            player (int): The player who is making the move.
            move (Tuple[int, int]): The coordinates of the move.
        """
        if self._is_valid_move(player, move):
            self._logger.info(
                "Player %s on board %s is making move %s", player, self._id, move
            )
            self._board[move[0]][move[1]] = player

    def _is_valid_move(self, player: int, move: Tuple[int, int]) -> bool:
        if player not in self._markers:
            self._handle_invalid_move(
                f"Player must be in {list(self._markers.keys())}: {player}"
            )
            return False
        if not (move[0] in [0, 1, 2] and move[1] in [0, 1, 2]):
            self._handle_invalid_move(f"Move value must be in [0, 1, 2]: {move}")
            return False
        if self._board[move[0]][move[1]] is not None:
            self._handle_invalid_move(
                f"Move {(player, move)} must be to an empty square, player "
                f"{self._board[move[0]][move[1]]} is their."
            )
            return False
        return True

    def _handle_invalid_move(self, message):
        message = f"Invalid move on board {self._id}:\n" + message
        self._logger.error(message)
        raise InvalidMoveError(message)

    def is_winner(self) -> Tuple[bool, Union[int, None]]:

        # TODO: Make nicer implementation of this, maybe inform people how they won.

        winner = None
        for i in range(3):
            if self._board[i][0] == self._board[i][1] == self._board[i][2] is not None:
                winner = self._check_winner(winner, self._board[i][0])
            if self._board[0][i] == self._board[1][i] == self._board[2][i] is not None:
                winner = self._check_winner(winner, self._board[0][i])
        if self._board[0][0] == self._board[1][1] == self._board[2][2] is not None:
            winner = self._check_winner(winner, self._board[0][0])
        if self._board[0][2] == self._board[1][1] == self._board[2][0] is not None:
            winner = self._check_winner(winner, self._board[0][2])

        if winner is not None:
            self._logger.info("Player %s has won on board %s", winner, self._id)
            return True, winner
        return False, None

    def _check_winner(
        self, current_winner: Union[int, None], next_winner: Union[int, None]
    ) -> Union[int, None]:

        # TODO: Raise error if winning diagonals don't overlap for the same
        # player.

        if next_winner is None:
            return None
        if current_winner is None:
            return next_winner
        if current_winner == next_winner:
            self._logger.info(
                f"Player {current_winner} won in multiple ways on board {self._id}."
            )
            return next_winner
        if current_winner != next_winner:
            self._logger.error(f"Multiple winners on the board {self._id}.")
            raise InvalidStateError("Multiple winners on the board.")

    def __repr__(self):
        return "\n--+---+--\n".join(
            [self._get_row_representation(row) for row in self._board]
        )

    def _get_row_representation(self, row: list) -> str:
        return " | ".join([self._get_marker(cell) for cell in row])

    def _get_marker(self, player: Union[int, None]) -> str:
        if player in self._markers:
            return self._markers[player]
        if player is None:
            return " "
        self._logger.warning(
            "On board %s invalid player value found: %s", self._id, player
        )
        return "?"
