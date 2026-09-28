#ifndef PRODUCTERROR_H
#define PRODUCTERROR_H

#include <stdexcept>
#include <string>

class ProductError : public std::exception {
public:
    ProductError(const std::string& message) : message(message) {}
    const char* what() const noexcept override {
        return message.c_str();
    }
private:
    std::string message;
};

#endif