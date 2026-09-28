#ifndef DATAIO_H
#define DATAIO_H

#include "warehouse.h"
#include "producterror.h"
#include "dvd.h"
#include "bluray.h"
#include <string>
#include <sstream>
#include <fstream>
#include <stdexcept>

class DataIO {
public:
    DataIO(Warehouse& warehouse);

    bool importData(const std::string& filename);

private:
    Warehouse& warehouse;

    // Komplette Zeile einlesen und Kategorie des Eintrags bestimmen
    void processLine(const std::string& line);

    // Aufteilung der Verarbeitung nach Kategorie ( Kunde / Produkte / Lager )
    // Kunde
    void processCustomer(std::istringstream& iss);
    // DVD
    void processDVD(std::istringstream& iss);
    // BluRay
    void processBluRay(std::istringstream& iss);
    // Lager
    void processStock(std::istringstream& iss);
};

#endif