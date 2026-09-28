#ifndef CUSTOMER_H
#define CUSTOMER_H

#include <string>

class Customer{
    public:
    Customer();
    Customer(int ident, std::string l, std::string f, std::string s, int snr, int pc, std::string c);

    // Getter (nur ID nötig)
    int getId() const;

    std::string toString() const;

    friend std::ostream& operator <<(std::ostream& os, const Customer& customer);

    private:
    int id;
    std::string l_name;
    std::string f_name;
    std::string street;
    int street_nr;
    int postal_code;
    std::string city;
};

#endif