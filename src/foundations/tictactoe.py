from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

Board = tuple[str, ...]
WIN_LINES = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


@dataclass(frozen=True)
class MoveResult:
    move: int
    score: int
    states: int


def winner(board: Board) -> str | None:
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    if " " not in board:
        return "draw"
    return None


def available_moves(board: Board) -> list[int]:
    return [i for i, cell in enumerate(board) if cell == " "]


def make_move(board: Board, move: int, player: str) -> Board:
    cells = list(board)
    cells[move] = player
    return tuple(cells)


def minimax_best_move(board: Board, player: str = "X") -> MoveResult:
    opponent = "O" if player == "X" else "X"
    states = 0

    @lru_cache(maxsize=None)
    def minimax(state: Board, turn: str) -> int:
        nonlocal states
        states += 1
        result = winner(state)
        if result == player:
            return 1
        if result == opponent:
            return -1
        if result == "draw":
            return 0
        scores = [minimax(make_move(state, move, turn), opponent if turn == player else player) for move in available_moves(state)]
        return max(scores) if turn == player else min(scores)

    scored = [(minimax(make_move(board, move, player), opponent), move) for move in available_moves(board)]
    score, move = max(scored)
    return MoveResult(move, score, states)


def alphabeta_best_move(board: Board, player: str = "X") -> MoveResult:
    opponent = "O" if player == "X" else "X"
    states = 0

    def search(state: Board, turn: str, alpha: int, beta: int) -> int:
        nonlocal states
        states += 1
        result = winner(state)
        if result == player:
            return 1
        if result == opponent:
            return -1
        if result == "draw":
            return 0
        if turn == player:
            value = -2
            for move in available_moves(state):
                value = max(value, search(make_move(state, move, turn), opponent, alpha, beta))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        value = 2
        for move in available_moves(state):
            value = min(value, search(make_move(state, move, turn), player, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

    best_score, best_move = -2, -1
    for move in available_moves(board):
        score = search(make_move(board, move, player), opponent, -2, 2)
        if score > best_score:
            best_score, best_move = score, move
    return MoveResult(best_move, best_score, states)
