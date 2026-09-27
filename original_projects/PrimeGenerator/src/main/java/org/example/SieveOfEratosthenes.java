package org.example;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;

/**
 * Das Sieb des Eratosthenes dient dazu, alle nicht-Primzahlen
 * in einem bestimmten Bereich zu eliminieren und so alle
 * Primzahlen auf eine schnelle Weise zu finden.
 * Verwendet man nun Nebenläufigkeit, so können parallel
 * Vielfache eliminiert werden, was die Effizienz steigert.
 */
class SieveOfEratosthenes implements Callable<List<Integer>> {
    private final int start;
    private final int end;

    public SieveOfEratosthenes(int st, int e) {
        start = st;
        end = e;
    }

    /**
     * Anwendung des Siebs von Eratosthenes
     * @return : Liste aller Primzahlen
     */
    @Override
    public List<Integer> call() {
        List<Integer> primes = new ArrayList<>();

        boolean[] isPrime = new boolean[end + 1];
        // Initialisiere alle Zahlen als prim
        for (int i = 2; i <= end; i++) {
            isPrime[i] = true;
        }

        // Wenn p prim: Es gibt keinen Teiler zu p der größer als sqrt(p)
        for (int p = 2; p * p <= end; p++) {
            if (isPrime[p]) {
                // Streiche alle Vielfachen dieser Primzahl
                // (Kleinere Vielfache durch vorherige Primzahl bereits gestrichen)
                for (int i = p * p; i <= end; i += p) {
                    isPrime[i] = false;
                }
            }
        }

        // Füge die Primzahlen 1 < p im Bereich zum Ergebnis hinzu
        for (int i = Math.max(2, start); i <= end; i++) {
            if (isPrime[i]) {
                System.out.println(i);
                primes.add(i);
            }
        }

        return primes;
    }
}