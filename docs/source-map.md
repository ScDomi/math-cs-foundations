# Source map

This repo is intentionally based on the old project material in `original_projects/`.

| Showcase module | Original project | Notes |
|---|---|---|
| `foundations.primes` | `original_projects/PrimeGenerator` | Python adaptation of the Java Eratosthenes/Atkin ideas, plus deterministic Miller-Rabin for a compact demo. |
| `foundations.search` | `original_projects/Suchalgorithmen` | Keeps the sequence-search theme and extends it into reusable graph-search functions for portfolio readability. |
| `foundations.tictactoe` | `original_projects/TicTacToeAI` | Python adaptation of the game-tree/minimax idea from the Java project. |
| `foundations.turmites` | `original_projects/Turmites` | Minimal importable Langton's Ant core; visual scripts/screenshots remain preserved in originals. |
| `original_projects/VierGewinntKI` | old Connect Four AI repo | Preserved as source material. Not yet normalized into the importable package. |

Adaptation rule: preserve old code under `original_projects/`; only adapt code into `src/foundations/` when needed for importability, tests, or CLI demos.
