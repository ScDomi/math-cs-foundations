#ifndef PRODUCT_H
#define PRODUCT_H

#include <iostream>
#include <string>
#include "producterror.h"

class Product{
    public:
    Product();
    Product(int ident, std::string t);
    virtual ~Product() = default;


    // String Repräsentation für Konsole / Dateiexport
    virtual std::string toString() const = 0;

    // Getter (nur ID und Titel nötig)
    int getId() const;
    std::string getTitle() const;

    // Überladung Ausgabeoperator für anschließende Nutzung für Konsole / Export
    // es wird sichergestellt, dass product während Ausgabe nicht verändert wird
    friend std::ostream& operator<<(std::ostream& os, const Product& product);

    protected:
    int id;
    std::string title;
};

#endif