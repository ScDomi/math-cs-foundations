#include "dataio.h"
#include <memory>

DataIO::DataIO(Warehouse& warehouse)
    : warehouse(warehouse) {}

bool DataIO::importData(const std::string& filename) {
    // öffne Datei
    std::ifstream inputFile(filename);
    if (!inputFile.is_open()) {
        std::cout << "Error opening file: " << filename << std::endl;
        return false;
    }

    std::string line;
    int lineNumber = 0;
        // zeilenweise einlesen
        while (std::getline(inputFile, line)) {
            ++lineNumber;
            try {
                // Zeile entsprechend verarbeiten
                processLine(line);
            } catch (const std::exception& e) {
                // lokale Fehlerbehandlung (Einlesen wird nicht abgebrochen)
                // fehlerhafte, doppelte Einträge und Leerzeilen werden erkannt
                std::cout << "Error processing line " << lineNumber << ": " << e.what() << std::endl;
            }
        }
    inputFile.close();
    return true;
}

// Komplette Zeile einlesen und Kategorie des Eintrags bestimmen
void DataIO::processLine(const std::string& line) {
    std::istringstream iss(line);
    std::string category;
    iss >> category;
    if (category == "Kunde") {
        processCustomer(iss);
    } else if (category == "DVD") {
        processDVD(iss);
    } else if (category == "Bluray") {
        processBluRay(iss);
    } else if (category == "Lager") {
        processStock(iss);
    } else {
        throw std::runtime_error("Unknown category: " + category);
    }
}

// Aufteilung der Verarbeitung nach Kategorie ( Kunde / Produkte / Lager )
// Kunde
void DataIO::processCustomer(std::istringstream& iss) {
    int id;
    std::string l_name, f_name, street, city;
    int street_nr, postal_code;
    if (!(iss >> id >> l_name >> f_name >> street >> street_nr >> postal_code >> city)) {
        throw std::runtime_error("Invalid customer entry: " + iss.str());
    }
    std::shared_ptr<Customer> customer = std::make_shared<Customer>(id, l_name, f_name, street, street_nr, postal_code, city);
    warehouse.addCustomer(customer);
}

// DVD
void DataIO::processDVD(std::istringstream& iss) {
    int id, minutes;
    std::string title;

    if (!(iss >> id >> title >> minutes)) {
        throw std::runtime_error("Invalid DVD entry: " + iss.str());
    }
    if (minutes < 0) {
        throw ProductError("Invalid DVD minutes: " + std::to_string(minutes));
    }

    std::shared_ptr<Product> dvd = std::make_shared<DVD>(id, title, minutes);
    warehouse.addProduct(dvd);
}

// BluRay
void DataIO::processBluRay(std::istringstream& iss) {
    int id, track_count;
    std::string title, resolution;

    if (!(iss >> id >> title >> track_count >> resolution)) {
        throw std::runtime_error("Invalid BluRay entry: " + iss.str());
    }

    if (track_count < 0) {
        throw ProductError("Invalid BluRay track count: " + std::to_string(track_count));
    }

    std::shared_ptr<Product> bluray = std::make_shared<BluRay>(id, title, track_count, resolution);
    warehouse.addProduct(bluray);
}

// Lager
void DataIO::processStock(std::istringstream& iss) {
    int productId, quantity;

    if (!(iss >> productId >> quantity)) {
        throw std::runtime_error("Invalid stock entry: " + iss.str());
    }

    warehouse.setStock(productId, quantity);
    }
