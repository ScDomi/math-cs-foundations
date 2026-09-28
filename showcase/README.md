# Multi-language showcase

This folder exists so the repository does not look like the old Java, Prolog and C++ work was hidden in an archive while only the Python rewrite counts.

The Python package is the clean demo layer, but these files are also part of the showcase: they show the same foundations in the languages they were originally implemented in.

## Java

`showcase/java/`

- `SieveOfEratosthenes.java` — classic prime sieve
- `SieveOfAtkin.java` — more advanced prime sieve using quadratic residues
- `ConcurrentPrimeChecker.java` — concurrent prime-checking structure from the original Java project
- `Board.java` / `Player.java` / `Computer.java` / `SmartComputer.java` — Tic-Tac-Toe board logic, player abstractions and AI decision-making

These files are lightly adjusted copies from the Maven projects in `original_projects/` so they are easier to inspect directly from GitHub.

## Prolog

`showcase/prolog/sudoku_solver.pl`

A CLP(FD)-based Sudoku solver for 4x4, 6x6 and 9x9 boards. This is intentionally kept in Prolog because constraint solving is exactly where Prolog makes sense.

## C++

`showcase/cpp/`

A small OOP/file-I/O inventory exercise showing typed modeling, inheritance-style structure and parsing/export logic. This stays C++ instead of being translated into Python because the point is the language range.

## Original sources

The fuller old projects are still preserved under `original_projects/`.

This folder is the readable front layer. `original_projects/` is the source archive.