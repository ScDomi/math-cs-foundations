from foundations.primes import miller_rabin, primes_trial, sieve_atkin, sieve_eratosthenes
from foundations.search import astar, breadth_first_search, dijkstra
from foundations.sudoku import is_valid_solution, solve_sudoku
from foundations.tictactoe import alphabeta_best_move, winner
from foundations.turmites import simulate


def test_prime_algorithms_agree_on_small_range():
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert primes_trial(30) == expected
    assert sieve_eratosthenes(30) == expected
    assert sieve_atkin(30) == expected
    assert miller_rabin(2_147_483_647)
    assert not miller_rabin(2_147_483_645)


def test_graph_search_finds_short_paths():
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["F"],
        "E": ["F"],
        "F": [],
    }
    result = breadth_first_search("A", lambda n: n == "F", lambda n: graph[n])
    assert result is not None
    assert result.path[0] == "A"
    assert result.path[-1] == "F"
    weighted = {"A": [("B", 3), ("C", 1)], "B": [("D", 1)], "C": [("D", 5)], "D": []}
    shortest = dijkstra("A", lambda n: n == "D", lambda n: weighted[n])
    assert shortest is not None
    assert shortest.path == ["A", "B", "D"]
    assert shortest.cost == 4
    a_star = astar("A", lambda n: n == "D", lambda n: weighted[n], lambda _: 0)
    assert a_star is not None
    assert a_star.cost == 4


def test_sudoku_solver_returns_valid_solution():
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
    assert solved is not None
    assert is_valid_solution(solved)


def test_tictactoe_alpha_beta_blocks_winning_line():
    board = ("X", "X", " ", "O", " ", " ", " ", " ", "O")
    assert winner(board) is None
    move = alphabeta_best_move(board, "O")
    assert move.move == 2


def test_langtons_ant_is_deterministic():
    grid, ant = simulate(10)
    assert len(grid) == 6
    assert (ant.row, ant.col, ant.direction) == (1, -1, 2)
