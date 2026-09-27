# C++ OOP Inventory Exercise

Small C++ exercise focused on typed object modeling, inheritance, smart pointers, file-based loading and export logic.

This is intentionally framed as a language-fundamentals example, not as a production warehouse product. The business domain is simple on purpose; the interesting part is the C++ structure around products, customers, stock entries and parser boundaries.

## What it demonstrates

- Object-oriented domain modeling in C++
- Abstract base class with `Product` plus concrete `DVD` and `BluRay` types
- `std::shared_ptr` usage for object ownership inside the warehouse catalog
- File parsing with validation and local error handling
- Separation between data loading (`DataIO`) and domain storage (`Warehouse`)
- Exporting the resulting object state back to a text file

## Source note

The code was copied from the original `WareHouseSystem` project and kept close to source. Only tiny polish changes were made where they improve build hygiene without changing the exercise:

- fixed the `BluRay` header guard casing
- added a virtual destructor to the abstract `Product` base class
- added this README for portfolio framing

## Build and run

From this directory:

```bash
c++ -std=c++17 -Wall -Wextra -pedantic *.cpp -o cpp_oop_inventory
./cpp_oop_inventory
```

The demo reads `acme.load`, prints imported customers/products/stock to stdout and writes `exported_warehouse_data.txt`.

`acme.load` intentionally contains a few malformed or duplicate-ish lines from the original exercise data, so the parser prints recoverable error messages and continues importing valid entries.
