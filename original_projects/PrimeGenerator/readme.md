# Concurrent Prime Checker (Sieb von Atkin)

## Beschreibung

Dieses Projekt implementiert einen Primzahlengenerator, welcher bis zu einer flexiblen Obergrenze mit einer gewünschten Anzahl an Threads alle Primzahlen generiert. Die Primzahlen können mithilfe zweier unterschiedlicher Algorithmen bestimmt werden:
- Sieb von Eratosthenes
- Sieb von Atkin
Das Sieb von Atkin berechnet die große Primzahlen sehr viel schneller als das Sieb des Eratosthenes. Zum Vergleich werden die Laufzeiten beider Algorithmen am Ende der Primzahlengeneration ausgegeben.

## Funktionalitäten

- Der Benutzer gibt die Obergrenze (eine positive Ganzzahl) für Primzahlen über die Kommandozeile ein.
- Der Benutzer gibt die Anzahl der zu verwendeten Threads über die Kommandozeile ein.
- Das Programm erstellt mehrere Threads, wobei jeder Thread einen Teil des Zahlenbereichs überprüft.
- Jeder Thread soll seine gefundenen Primzahlen auf der Konsole ausgeben.
- Das Hauptprogramm soll am Ende alle gefundenen Primzahlen sortiert auflisten.

## Versionen der technischen Vorraussetzungen

- OpenJDK 21.0.1 2023-10-17
- OpenJDK Runtime Environment Homebrew (build 21.0.1)
- OpenJDK 64-Bit Server VM Homebrew (build 21.0.1, mixed mode, sharing)
- IntelliJ IDEA 2023.3.2 (Ultimate Edition)
- Builttool: Maven

## Verwendung

1. Öffnen sie das Projekt in einer IDE (IntelliJ wurde bei der Erstellung verwendet)

2. Führen Sie die Main-Methode in der Klasse ConcurrentPrimeChecker aus.

3. Auf der Konsole wird nun etwas angezeigt. Folgen sie den Anweisungen.

## Autor

- Dominik Schwagerl
