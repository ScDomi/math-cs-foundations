#include "dvd.h"

DVD::DVD()
    : Product(), minutes(-1){}
DVD::DVD(int ident, std::string t, int min)
    : Product(ident, t), minutes(min){}

    // String Repräsentation für Konsole / Dateiexport
    // Format bleibt gleich dem Dateiformat
std::string DVD::toString() const {
    std::string str;
    str += "DVD " + std::to_string(id) + " " + title + " " + std::to_string(minutes)+ '\n';
    return str;
}