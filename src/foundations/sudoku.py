from __future__ import annotations

Grid = list[list[int]]


def candidates(board: Grid, row: int, col: int) -> set[int]:
    if board[row][col] != 0:
        return {board[row][col]}
    size = len(board)
    box_h = box_w = int(size**0.5)
    used = set(board[row]) | {board[r][col] for r in range(size)}
    start_r, start_c = (row // box_h) * box_h, (col // box_w) * box_w
    used |= {board[r][c] for r in range(start_r, start_r + box_h) for c in range(start_c, start_c + box_w)}
    return set(range(1, size + 1)) - used


def find_mrv_cell(board: Grid) -> tuple[int, int, set[int]] | None:
    best = None
    for r, row in enumerate(board):
        for c, value in enumerate(row):
            if value == 0:
                opts = candidates(board, r, c)
                if not opts:
                    return (r, c, opts)
                if best is None or len(opts) < len(best[2]):
                    best = (r, c, opts)
    return best


def solve_sudoku(board: Grid) -> Grid | None:
    """Backtracking Sudoku solver using the MRV heuristic."""
    board = [row[:] for row in board]

    def backtrack() -> bool:
        cell = find_mrv_cell(board)
        if cell is None:
            return True
        row, col, opts = cell
        for value in sorted(opts):
            board[row][col] = value
            if backtrack():
                return True
            board[row][col] = 0
        return False

    return board if backtrack() else None


def is_valid_solution(board: Grid) -> bool:
    size = len(board)
    target = set(range(1, size + 1))
    box = int(size**0.5)
    rows = all(set(row) == target for row in board)
    cols = all({board[r][c] for r in range(size)} == target for c in range(size))
    boxes = all(
        {board[r][c] for r in range(br, br + box) for c in range(bc, bc + box)} == target
        for br in range(0, size, box)
        for bc in range(0, size, box)
    )
    return rows and cols and boxes
