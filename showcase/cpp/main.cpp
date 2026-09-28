/************************************************
 * Name: Dominik Schwagerl
 * Studiengang: Bachelor Künstliche Intelligenz
*************************************************/

#include "customer.h"
#include "product.h"
#include "warehouse.h"
#include "dataio.h"
#include "producterror.h"
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <map>
#include <memory>
#include <fstream>
#include <sstream>
#include <stdexcept>

int main() {
    // Initialisiere Lagersystem und Datenverarbeitung
    Warehouse warehouse;
    DataIO dataIO(warehouse);

    // Datei laden (mit Fehlerbehandlung)
    std::string filename = "./acme.load";
    bool importSuccess = dataIO.importData(filename);
    if (importSuccess) {
        std::cout << "Data imported successfully from file: " << filename << std::endl;
    } else {
        std::cout << "Failed to import data from file: " << filename << std::endl;
        return 1;   // Zeigt Fehler an
    }

    // Erzeuge Beispiele
    std::shared_ptr<DVD> d1 = std::make_shared<DVD>(1, "Example DVD", 120);
    std::shared_ptr<BluRay> b1 = std::make_shared<BluRay>(20, "Example BluRay", 102, "4K");

    std::shared_ptr<Customer> c1 = std::make_shared<Customer>(100, "Mustermann", "Max", "Musterstr.", 1, 11211, "Musterstadt");
    // Füge Beispiele in das Lagersystem ein
    warehouse.addProduct(d1);
    warehouse.addCustomer(c1);
    warehouse.addProduct(b1);

    // Ausgabe aktueller Inhalt Lagersystem
    std::cout << "Current Warehouse Contents:\n";
    //std::cout << warehouse.getAllObjectsAsString() << std::endl;
    warehouse.getCustomers();
    warehouse.getProducts();
    // Ausgabe des Lagerbestands mit Produktbezeichnung
    warehouse.getStock();

    // Exportiere Lagersystem in neue Datei (mit Fehlerbehandlung)
    std::string exportFilename = "exported_warehouse_data.txt";
    warehouse.exportData(exportFilename);
    std::cout << "Warehouse data exported to file: " << exportFilename << std::endl;

    return 0; 
}