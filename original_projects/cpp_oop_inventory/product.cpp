#include "product.h"

Product::Product()
    : id{-1}, title{"--"}{}
Product::Product(int ident, std::string t)
    : id(ident), title(t){}

// Getter (nur ID und Titel nötig)
int Product::getId() const { return id; }
std::string Product::getTitle() const { return title; }

// Überladung Ausgabeoperator für anschließende Nutzung für Konsole / Export
// es wird sichergestellt, dass product während Ausgabe nicht verändert wird
std::ostream& operator<<(std::ostream& os, const Product& product) {
    // Formatierung des Ausgabestroms durch String Repräsentation
    os << product.toString();
    return os;
}
