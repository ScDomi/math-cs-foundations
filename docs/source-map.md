# Source map

This repo is intentionally based on the old project material in `original_projects/`.

| Showcase module | Original project | Notes |
|---|---|---|
| `foundations.primes` | `original_projects/PrimeGenerator` | Python adaptation of the Java Eratosthenes/Atkin ideas, plus deterministic Miller-Rabin for a compact demo. |
| `foundations.sequence_search` | `original_projects/Suchalgorithmen` | Directly modernizes the old sequence-search scripts: linear, sentinel, binary, exponential and interpolation search. |
| `foundations.search` | `original_projects/Suchalgorithmen` | Extends the search theme into reusable graph-search functions: BFS, DFS, Dijkstra and A*. |
| `foundations.sudoku` | Python showcase module | Compact MRV/backtracking implementation for the tested package layer. |
| `original_projects/SudokuSolverProlog` | `original_projects/SudokuSolverProlog` | Original Prolog CLP(FD) Sudoku solver for 4x4, 6x6 and 9x9 puzzles. |
| `foundations.tictactoe` | `original_projects/TicTacToeAI` | Python adaptation of the game-tree/minimax idea from the Java project. |
| `foundations.turmites` | `original_projects/Turmites` | Minimal importable Langton's Ant core; visual scripts/screenshots remain preserved in originals. |
| `original_projects/VierGewinntKI` | old Connect Four AI repo | Preserved as source material. Not yet normalized into the importable package. |

Adaptation rule: preserve old code under `original_projects/`; only adapt code into `src/foundations/` when needed for importability, tests, or CLI demos.
