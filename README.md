# Math & CS Foundations

A curated showcase repo built from Domi's older foundations projects. The goal is not to pretend this is a giant framework: it is a clean archive + small reusable Python package around classic algorithms, search, game AI and cellular automata.

## What is inside

- `original_projects/` keeps the old project code close to the source material.
  - `Suchalgorithmen`: sequence search algorithms in Python.
  - `PrimeGenerator`: Java implementations of Eratosthenes, Atkin and concurrent prime checks.
  - `TicTacToeAI`: Java Tic-Tac-Toe with tests and a smarter computer player.
  - `Turmites`: Langton's Ant / turmite experiments and generated screenshots.
  - `VierGewinntKI`: Connect Four AI experiments.
- `src/foundations/` contains a lightweight Python package with the parts that are useful to import, test and demo.
- `tests/` contains smoke-level regression tests so the repo stays runnable.

## Design choice

The old code is intentionally preserved in `original_projects/`. The showcase package only adapts where it makes the repo easier to run from a modern Python environment: small type hints, importable functions, deterministic tests and no GUI dependency in the default path.

## Quick start

```bash
python -m pip install -e '.[dev]'
pytest
foundations demo
```

No dataset downloads, no heavyweight dependencies. `matplotlib` is optional and only needed for visual turmite experiments.

## Demo examples

```python
from foundations.primes import sieve_eratosthenes, sieve_atkin, miller_rabin
from foundations.search import breadth_first_search
from foundations.sudoku import solve_sudoku
from foundations.tictactoe import alphabeta_best_move
from foundations.turmites import simulate

assert sieve_eratosthenes(30) == sieve_atkin(30)
assert miller_rabin(2_147_483_647)
```

## Verification

This repo is meant to be boringly verifiable:

```bash
python -m compileall src tests
pytest
```

## Repo status

Portfolio polish is in progress. Current priorities before public release:

1. Keep original source projects intact, without committing private review PDFs or build junk.
2. Add CI for compile + tests.
3. Add short notes explaining which original project each adapted module came from.
4. Optionally publish as `math-cs-foundations` after final review.
