#include "warehouse.h"


// Methoden zum Einfügen neuer Instanzen
void Warehouse::addCustomer(std::shared_ptr<Customer> customer) {
    customers[customer->getId()] = customer;
}

void Warehouse::addProduct(std::shared_ptr<Product> product) {
    products.push_back(product);
}

void Warehouse::setStock(int productId, int quantity) {
    stock[productId] = quantity;
}

// Seperate Methoden zur Ausgabe Kunden/Produktkatalog/Lagerbestand
// Ausgabe der Kunden
void Warehouse::getCustomers() {
    std::string cst;
    cst += "Customers:\n";
    for (const auto& pair : customers) {
        cst += pair.second->toString() + "\n";
    }
    std::cout << cst << std::endl;
}
// Ausgabe des Produktkatalogs
void Warehouse::getProducts() {
    std::string prd;
    prd += "Product Catalog:\n";
    for (const auto& product : products) {
        prd += product->toString() + "\n";
    }
    std::cout << prd << std::endl;
}
// Ausgabe des Lagerbestands mit jeweils passenden Produktbezeichnern
void Warehouse::getStock() {
    std::string stk;
    stk += "Stock:\n";
    for (const auto& pair : stock) {
        int productId = pair.first;
        int quantity = pair.second;
        // Produkt nach id suchen
        std::string productTitle = getProductTitleById(productId);
        std::cout << "Lager " << productId << " " << quantity << " " << productTitle << "\n";
    }
}

std::string Warehouse::getAllObjectsAsString() const {
    std::string result;

    // Customers
    result += "Customers:\n";
    for (const auto& pair : customers) {
        result += pair.second->toString() + "\n";
    }

    // Products
    result += "Product Catalog:\n";
    for (const auto& product : products) {
        result += product->toString() + "\n";
    }

    // Stock
    result += "Stock:\n";
    for (const auto& pair : stock) {
        int productId = pair.first;
        int quantity = pair.second;
        result += "Lager " + std::to_string(productId) + " " + std::to_string(quantity) + "\n";
    }
    return result;
}

void Warehouse::exportData(const std::string& filename) const {
    //öffne Datei
    std::ofstream outputFile(filename);
    if (!outputFile.is_open()) {
        std::cout << "Error opening file: " << filename << std::endl;
        return;
    }

    // Exportiere Kunden
    outputFile << "Customers:\n";
    for (const auto& pair : customers) {
        outputFile << pair.second->toString() << "\n";
    }

    // Exportiere Produktkatalog
    outputFile << "Product Catalog:\n";
    for (const auto& product : products) {
        outputFile << product->toString() << "\n";
    }

    // Exportiere Lagerbestand
    outputFile << "Stock:\n";
    for (const auto& pair : stock) {
            int productId = pair.first;
            int quantity = pair.second;
            outputFile << "Lager " << productId << " " << quantity << "\n";
        }

    outputFile.close();
}

// Suche nach Produkt mit bestimmter Id
std::string Warehouse::getProductTitleById(int productId) const {
    for (const auto& product : products) {
        if (product->getId() == productId) {
            return product->toString();
        }
    }
    return "Product not found";
}

