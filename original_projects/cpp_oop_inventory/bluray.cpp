#include "bluray.h"


BluRay::BluRay()
    : Product(), track_count(-1), res("0x0"){}
BluRay::BluRay(int ident, std::string t, int c, std::string r)
    : Product(ident, t), track_count(c), res(r){}

// String Repräsentation für Konsole / Dateiexport
// Format bleibt gleich dem Dateiformat
std::string BluRay::toString() const {
    std::string str;
    str += "BluRay " + std::to_string(id) + " " + title + " " + std::to_string(track_count) + " " + res + '\n';
    return str;
}