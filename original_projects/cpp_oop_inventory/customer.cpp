#include "customer.h"

Customer::Customer()
    : id(-1), l_name("--"), f_name("--"), street("--"), street_nr(-1), postal_code(-1), city("--"){}
Customer::Customer(int ident, std::string l, std::string f, std::string s, int snr, int pc, std::string c)
    : id(ident), l_name(l), f_name(f), street(s), street_nr(snr), postal_code(pc), city(c){}

// Getter (nur ID nötig)
int Customer::getId() const { return id; }

std::string Customer::toString() const{
    std::string str;
    str = "Kunde " + std::to_string(id) + " " + l_name + " " + f_name + " " + street + " " + std::to_string(street_nr) + " " + std::to_string(postal_code) + " " + city + "\n";
    return str;
}

std::ostream& operator<<(std::ostream& os, const Customer& customer){
    os << customer.toString();
    return os;
}
