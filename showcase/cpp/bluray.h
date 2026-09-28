#ifndef BLURAY_H
#define BLURAY_H

#include "product.h"

class BluRay: public Product{
    public:
    BluRay();
    BluRay(int ident, std::string t, int c, std::string r);

    // String Repräsentation für Konsole / Dateiexport
    // Format bleibt gleich dem Dateiformat
    std::string toString() const override;

    private:
    int track_count;
    std::string res;
};

#endif 