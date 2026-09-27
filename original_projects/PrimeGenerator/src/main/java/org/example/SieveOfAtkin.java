package org.example;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;

/**
 * Das Sieb des Atkin dient ebenfalls dazu, alle nicht-Primzahlen
 * zu eliminieren. Allerdings handelt es sich einen moderneren
 * Algorithmus, welcher bei großen Zahlen deutlich schneller zum
 * Ergebnis kommt.
 */
class SieveOfAtkin implements Callable<List<Integer>> {
    private final int start;
    private final int end;

    public SieveOfAtkin(int start, int end) {
        this.start = start;
        this.end = end;
    }

    /**
     * Anwendung des Siebs von Atkin
     * @return : Liste aller Primzahlen
     */
    @Override
    public List<Integer> call() {
        List<Integer> primes = new ArrayList<>();

        // Sieb des Atkin
        boolean[] isPrime = new boolean[end + 1];
        int limit = (int) Math.sqrt(end) + 1;

        // Sieb von Atkin kann 2 und 3 nicht als Primzahl erkennen
        if(end == 2){
            primes.add(2);
        } else {
            primes.add(2);
            primes.add(3);
        }

        // Überprüfe auf Lösung der spezifischen Gleichungen
        // Invertiere Primzahlen-Wahrheitswert, falls Gleichung erfüllt
        for (int x = 1; x < limit; x++) {
            for (int y = 1; y < limit; y++) {
                int n = 4 * x * x + y * y;
                if (n <= end && (1 == n % 12 || 5 == n % 12)) {
                    isPrime[n] = !isPrime[n];
                }

                n = 3 * x * x + y * y;
                if (n <= end && n % 12 == 7) {
                    isPrime[n] = !isPrime[n];
                }

                n = 3 * x * x - y * y;
                if (x > y && n <= end && n % 12 == 11) {
                    isPrime[n] = !isPrime[n];
                }
            }
        }

        for (int n = 5; n <= limit; n++) {
            if (isPrime[n]) {
                for (int k = n * n; k <= end; k += n * n) {
                    isPrime[k] = false;
                }
            }
        }

        // Primzahlen zum Endergebnis hinzufügen
        for (int i = Math.max(2, start); i <= end; i++) {
            if (isPrime[i]) {
                primes.add(i);
            }
        }

        return primes;
    }
}
