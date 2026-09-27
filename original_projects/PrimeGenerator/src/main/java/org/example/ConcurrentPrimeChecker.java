/**
 * Aufgabe 4
 * Optimierter Concurrent Prime Checker (Sieb von Atkin)
 * @author Dominik Schwagerl
 * @since 2024-01-17
 */

package org.example;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.*;

/**
 * Lässt alle Primzahlen bis zu einer benutzerdefinierten
 * Obergrenze mithilfe einer gewünschten Anzahl an Threads
 * ausgeben; Der Zahlenbereich wird an die Threads aufgeteilt,
 * wobei jeder Thread einen Zahlenbereich übernimmt
 * OUT: Die Zahlen werden sortiert aufgelistet.
 */
class ConcurrentPrimeChecker {

    public static void main(String[] args) {
        // Bestimmung der Obergrenze und der Anzahl an Threads durch Konsolen-Eingabe

        Scanner input = new Scanner(System.in);
        System.out.println("Geben Sie eine ganze Zahl als Obergrenze für die Primzahlen ein: ");
        int limit = input.nextInt();
        System.out.println("Geben sie eine Anzahl an Threads ein: ");
        int threadCount = input.nextInt();
        input.close();

        List<Integer> primes;

        // Zeitmessung
        // es entsteht hier eine Warnung, welche gekonnt ignoriert werden soll
        // die Priorität wird hier auf korrekte Zeitmessung gelegt.
        long startTimeEratos = System.currentTimeMillis();
        primes = getPrimes(limit, threadCount, true);
        long endTimeEratos = System.currentTimeMillis();

        long startTimeAtkin = System.currentTimeMillis();
        primes = getPrimes(limit, threadCount, false);
        long endTimeAtkin = System.currentTimeMillis();

        // Ausgabe der gefundenen Primzahlen
        System.out.println("Primzahlen bis " + limit + ": " + primes);
        System.out.println("Laufzeit für den Sieb des Eratosthenes: " + (endTimeEratos-startTimeEratos) + " ms");
        System.out.println("Laufzeit für den Sieb des Atkin: " + (endTimeAtkin-startTimeAtkin) + " ms");
    }

    /**
     * Berechnet über mehrere Threads alle Primzahlen mithilfe des Siebs von Eratosthenes oder des Siebs von Atkin
     *
     * @param limit : Obergrenze
     * @param threadCount : Anzahl der Threads
     * @param useEratos : true für Sieb von Eratosthenes, false für Sieb von Atkin
     * @return Primzahlen
     */
    public static List<Integer> getPrimes(int limit, int threadCount, boolean useEratos) {
        List<Integer> primes = new ArrayList<>();
        List<Callable<List<Integer>>> tasks = new ArrayList<>();

        try (ExecutorService executor = Executors.newFixedThreadPool(threadCount)) {
            // Teile den Bereich der Primzahlen linear auf die Threads auf
            for (int i = 0; i < threadCount - 1; i++) {
                int low = i * (limit / threadCount) + 1;
                int high = (i + 1) * (limit / threadCount);
                tasks.add(useEratos ? new SieveOfEratosthenes(low, high) : new SieveOfAtkin(low, high));
            }
            // Letzter Bereich explizit Berechnen aufgrund der Rundungsfehler
            int lastLow = (threadCount - 1) * (limit / threadCount);
            tasks.add(useEratos ? new SieveOfEratosthenes(lastLow, limit) : new SieveOfAtkin(lastLow, limit));
            try {
                // Starten der Threads, Sammeln von Ergebnissen
                List<Future<List<Integer>>> results = executor.invokeAll(tasks);

                for (Future<List<Integer>> result : results) {
                    primes.addAll(result.get());
                }
            } catch (InterruptedException | ExecutionException e) {
                System.out.println("Es ist ein Fehler aufgetreten: " + e.getMessage());
            } finally {
                executor.shutdown();
            }
        }
        return primes;
    }
}
