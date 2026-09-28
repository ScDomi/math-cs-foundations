# Math & CS Foundations

A curated multi-language showcase repo built from Domi's older foundations projects. It is intentionally small and transparent: classic computer-science building blocks in Python, Java, Prolog and C++, with preserved original coursework code plus cleaned showcase files that make the ideas readable without hiding the languages they were actually built in.

## Foundation map

| Foundation | What it demonstrates | Showcase layer | Original source |
|---|---|---|---|
| Prime generation | Trial division, Sieve of Eratosthenes, Sieve of Atkin, deterministic Miller-Rabin | Python package + Java showcase files | `original_projects/PrimeGenerator` |
| Sequence search | Linear, sentinel, binary, exponential and interpolation search | Python package | `original_projects/Suchalgorithmen` |
| Graph search | BFS, DFS, Dijkstra and A* with path reconstruction | Python package | Extended from the search-algorithm theme |
| Constraint solving | Sudoku backtracking with minimum-remaining-values heuristic; CLP(FD) Sudoku in Prolog | Python package + Prolog showcase file | `original_projects/SudokuSolverProlog` |
| Game AI | Tic-Tac-Toe minimax and alpha-beta pruning | Python package + Java showcase files | `original_projects/TicTacToeAI` |
| Cellular automata | Langton's Ant / turmite simulation core | Python package | `original_projects/Turmites` |
| C++ OOP & File I/O | Typed object modeling, inheritance, file parsing and export logic | C++ showcase files | `original_projects/cpp_oop_inventory` |
| Adversarial game experiments | Connect Four AI experiments preserved as source material | original-only for now | `original_projects/VierGewinntKI` |

## Repository layout

```text
.
├── original_projects/        # old project code preserved close to source, incl. Java/Prolog/C++
├── showcase/                 # readable front-layer examples in the original languages
├── src/foundations/          # importable, tested Python showcase package
├── tests/                    # regression/smoke tests for every foundation area
├── docs/source-map.md        # exact mapping from old projects to showcase modules
├── docs/language-map.md      # Python / Java / Prolog overview
└── .github/workflows/ci.yml  # compile + pytest on Python 3.10-3.12
```

## Why this structure

The point is not to rewrite history and pretend the old projects were one perfectly planned framework. The old code stays visible in `original_projects/`. The `showcase/` folder highlights selected Java, Prolog and C++ files directly, because the language range is part of the signal. The Python package in `src/foundations/` adds a small testable demo layer on top; it does not replace the original-language work.

That makes the repo understandable in three layers:

1. **Original layer:** real old projects, mostly untouched.
2. **Language showcase layer:** selected Java, Prolog and C++ files cleaned just enough to inspect quickly.
3. **Python demo layer:** importable package, tests and CLI so the concepts are obvious in 30 seconds.

## Languages represented

This is not a Python-only dump. The repo currently includes:

- **Python**: importable package, tests, CLI, search algorithms, turmites and Connect Four experiments.
- **Java**: original PrimeGenerator and TicTacToeAI projects with Maven/test structure.
- **Prolog**: CLP(FD)-based Sudoku solver for 4x4, 6x6 and 9x9 puzzles.
- **C++**: compact OOP/file-I/O inventory exercise, framed as typed language-fundamentals work.

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
- Added `docs/language-map.md` so reviewers see Python, Java, Prolog and C++ at a glance.
- Connect Four is preserved as source material but not normalized into the importable package yet.
- C++ is included as `original_projects/cpp_oop_inventory`: close to the original project, with only tiny build-hygiene fixes and clearer portfolio framing.
