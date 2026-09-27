#ifndef WAREHOUSE_H
#define WAREHOUSE_H

#include "product.h"
#include "customer.h"
#include <map>
#include <vector>
#include <memory>
#include <fstream>

class Warehouse {
public:
// Methoden zum Einfügen neuer Instanzen
    void addCustomer(std::shared_ptr<Customer> customer);

    void addProduct(std::shared_ptr<Product> product);

    void setStock(int productId, int quantity);

// Seperate Methoden zur Ausgabe Kunden/Produktkatalog/Lagerbestand
    // Ausgabe der Kunden
    void getCustomers();
    // Ausgabe des Produktkatalogs
    void getProducts();
    // Ausgabe des Lagerbestands mit jeweils passenden Produktbezeichnern
    void getStock();

    std::string getAllObjectsAsString() const;

    void exportData(const std::string& filename) const;

private:

    // Suche nach Produkt mit bestimmter Id
    std::string getProductTitleById(int productId) const;

    // Speichert Kunden
    std::map<int, std::shared_ptr<Customer>> customers;
    // Speichert Produkte in Produktkatalog
    std::vector<std::shared_ptr<Product>> products;
    // Speichert Lagerbestand in seperaten Containerobjekt
    std::map<int, int> stock;
};

#endif