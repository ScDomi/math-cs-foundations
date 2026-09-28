# Source map

This repo is intentionally based on the old project material in `original_projects/`.

| Showcase layer | Original project | Notes |
|---|---|---|
| `showcase/java/SieveOf*.java`, `showcase/java/ConcurrentPrimeChecker.java` | `original_projects/PrimeGenerator` | Java prime-generation code kept visible as Java, with package lines removed only so the files are easier to inspect directly. |
| `foundations.primes` | `original_projects/PrimeGenerator` | Python demo adaptation of the Java Eratosthenes/Atkin ideas, plus deterministic Miller-Rabin for a compact tested CLI demo. |
| `foundations.sequence_search` | `original_projects/Suchalgorithmen` | Directly modernizes the old sequence-search scripts: linear, sentinel, binary, exponential and interpolation search. |
| `foundations.search` | `original_projects/Suchalgorithmen` | Extends the search theme into reusable graph-search functions: BFS, DFS, Dijkstra and A*. |
| `showcase/prolog/sudoku_solver.pl` | `original_projects/SudokuSolverProlog` | Prolog CLP(FD) Sudoku solver kept in Prolog because the constraint-programming language is part of the point. |
| `foundations.sudoku` | Python showcase module | Compact MRV/backtracking implementation for the tested package layer. |
| `showcase/java/Board.java`, `showcase/java/SmartComputer.java` | `original_projects/TicTacToeAI` | Java board/game-AI logic kept visible as Java, not buried as archived coursework only. |
| `foundations.tictactoe` | `original_projects/TicTacToeAI` | Python adaptation of the game-tree/minimax idea from the Java project. |
| `foundations.turmites` | `original_projects/Turmites` | Minimal importable Langton's Ant core; visual scripts/screenshots remain preserved in originals. |
| `showcase/cpp/` | old `WareHouseSystem` repo | Selected C++ OOP/file-I/O files surfaced as showcase material. |
| `original_projects/cpp_oop_inventory` | old `WareHouseSystem` repo | Fuller original C++ exercise preserved close to source and reframed as typed language-fundamentals work. |
| `original_projects/VierGewinntKI` | old Connect Four AI repo | Preserved as source material. Not yet normalized into the importable package. |

Adaptation rule: preserve old code under `original_projects/`; only adapt code into `src/foundations/` when needed for importability, tests, or CLI demos.
