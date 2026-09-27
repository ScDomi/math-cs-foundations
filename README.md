# Math & CS Foundations

A curated multi-language showcase repo built from Domi's older foundations projects. It is intentionally small and transparent: multiple classic computer-science building blocks, preserved original coursework code, plus a modern testable Python package that demonstrates the same ideas without forcing people to run old IDE projects.

## Foundation map

| Foundation | What it demonstrates | Showcase module | Original source |
|---|---|---|---|
| Prime generation | Trial division, Sieve of Eratosthenes, Sieve of Atkin, deterministic Miller-Rabin | `foundations.primes` | `original_projects/PrimeGenerator` |
| Sequence search | Linear, sentinel, binary, exponential and interpolation search | `foundations.sequence_search` | `original_projects/Suchalgorithmen` |
| Graph search | BFS, DFS, Dijkstra and A* with path reconstruction | `foundations.search` | Extended from the search-algorithm theme |
| Constraint solving | Sudoku backtracking with minimum-remaining-values heuristic in Python; CLP(FD) Sudoku in Prolog | `foundations.sudoku`, `original_projects/SudokuSolverProlog` | Python showcase + Prolog source project |
| Game AI | Tic-Tac-Toe minimax and alpha-beta pruning | `foundations.tictactoe` | `original_projects/TicTacToeAI` |
| Cellular automata | Langton's Ant / turmite simulation core | `foundations.turmites` | `original_projects/Turmites` |
| Adversarial game experiments | Connect Four AI experiments preserved as source material | original-only for now | `original_projects/VierGewinntKI` |

## Repository layout

```text
.
├── original_projects/        # old project code preserved close to source
├── src/foundations/          # importable, tested Python showcase package
├── tests/                    # regression/smoke tests for every foundation area
├── docs/source-map.md        # exact mapping from old projects to showcase modules
├── docs/language-map.md      # Python / Java / Prolog overview
└── .github/workflows/ci.yml  # compile + pytest on Python 3.10-3.12
```

## Why this structure

The point is not to rewrite history and pretend the old projects were one perfectly planned framework. The old code stays visible in `original_projects/`. The package in `src/foundations/` adapts only what helps the repo be readable, importable, testable and easy to demo.

That makes the repo understandable in two layers:

1. **Archive layer:** real old projects, mostly untouched.
2. **Showcase layer:** cleaned interface, tests and CLI so the foundations are obvious in 30 seconds.

## Languages represented

This is not a Python-only dump. The repo currently includes:

- **Python**: importable package, tests, CLI, search algorithms, turmites and Connect Four experiments.
- **Java**: original PrimeGenerator and TicTacToeAI projects with Maven/test structure.
- **Prolog**: CLP(FD)-based Sudoku solver for 4x4, 6x6 and 9x9 puzzles.

See `docs/language-map.md` for the exact map.

## Quick start

```bash
python -m pip install -e '.[dev]'
pytest
foundations
```

No dataset downloads, no heavyweight runtime dependencies. `matplotlib` is optional and only needed for visual turmite experiments from the older scripts.

## Demo output

The CLI intentionally touches several foundations in one run:

```text
Math & CS foundations demo
primes <= 50: [...]
Atkin matches Eratosthenes: True
sequence-search indices for 18: {'linear': 9, 'binary': 9, 'interpolation': 9}
alpha-beta chooses move ...
Langton ant after 100 steps: ...
Sudoku solved: True
```

## Python examples

```python
from foundations.primes import sieve_eratosthenes, sieve_atkin, miller_rabin
from foundations.sequence_search import binary_search, interpolation_search
from foundations.search import breadth_first_search, dijkstra, astar
from foundations.sudoku import solve_sudoku
from foundations.tictactoe import alphabeta_best_move
from foundations.turmites import simulate

assert sieve_eratosthenes(30) == sieve_atkin(30)
assert miller_rabin(2_147_483_647)
assert binary_search(list(range(0, 41, 2)), 18) == 9
assert interpolation_search(list(range(0, 41, 2)), 18) == 9
```

## Verification

```bash
python -m compileall src tests
pytest
```

CI runs the same compile/test path on Python 3.10, 3.11 and 3.12.

## Current public-readiness notes

- Kept old source projects, but removed private review PDFs and build junk.
- Added tests that cover each showcased foundation area.
- Added `docs/source-map.md` so reviewers can see what came from where.
- Added `docs/language-map.md` so reviewers see Python, Java and Prolog at a glance.
- Connect Four is preserved as source material but not normalized into the importable package yet.
- C++ is not included yet because no personal C++ source project was found under `/Users/domiai/Documents/workspace` during this pass.
