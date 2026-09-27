from __future__ import annotations

from dataclasses import dataclass

Direction = tuple[int, int]


@dataclass(frozen=True)
class Ant:
    row: int
    col: int
    direction: int = 0  # 0 up, 1 right, 2 down, 3 left


DIRECTIONS: tuple[Direction, ...] = ((-1, 0), (0, 1), (1, 0), (0, -1))


def step(grid: set[tuple[int, int]], ant: Ant) -> Ant:
    """One Langton's Ant step on an unbounded grid.

    White square: turn right and flip to black. Black square: turn left and flip
    to white. Then move forward.
    """
    position = (ant.row, ant.col)
    if position in grid:
        grid.remove(position)
        direction = (ant.direction - 1) % 4
    else:
        grid.add(position)
        direction = (ant.direction + 1) % 4
    dr, dc = DIRECTIONS[direction]
    return Ant(ant.row + dr, ant.col + dc, direction)


def simulate(steps: int) -> tuple[set[tuple[int, int]], Ant]:
    grid: set[tuple[int, int]] = set()
    ant = Ant(0, 0, 0)
    for _ in range(steps):
        ant = step(grid, ant)
    return grid, ant
