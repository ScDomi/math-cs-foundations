#ifndef DVD_H
#define DVD_H

#include "product.h"
#include <iostream>
#include <string>

class DVD: public Product{
    public:
    DVD();
    DVD(int ident, std::string t, int min);

    // String Repräsentation für Konsole / Dateiexport
    // Format bleibt gleich dem Dateiformat
    std::string toString() const override;

    private:
    int minutes;
};

#endif 