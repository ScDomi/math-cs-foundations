from __future__ import annotations

from .primes import sieve_atkin, sieve_eratosthenes
from .sequence_search import binary_search, interpolation_search, linear_search
from .sudoku import is_valid_solution, solve_sudoku
from .tictactoe import alphabeta_best_move
from .turmites import simulate


def main() -> None:
    primes_e = sieve_eratosthenes(50)
    primes_a = sieve_atkin(50)
    sequence = list(range(0, 41, 2))
    sequence_hits = {
        "linear": linear_search(sequence, 18),
        "binary": binary_search(sequence, 18),
        "interpolation": interpolation_search(sequence, 18),
    }
    board = (
        ("X", "O", "X"),
        (" ", "O", " "),
        (" ", "X", " "),
    )
    flat_board = tuple(cell for row in board for cell in row)
    move = alphabeta_best_move(flat_board, "O")
    grid, ant = simulate(100)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    solved = solve_sudoku(puzzle)
    print("Math & CS foundations demo")
    print(f"primes <= 50: {primes_e}")
    print(f"Atkin matches Eratosthenes: {primes_a == primes_e}")
    print(f"sequence-search indices for 18: {sequence_hits}")
    print(f"alpha-beta chooses move {move.move} after visiting {move.states} states")
    print(f"Langton ant after 100 steps: {len(grid)} black cells, ant={ant}")
    print(f"Sudoku solved: {solved is not None and is_valid_solution(solved)}")
