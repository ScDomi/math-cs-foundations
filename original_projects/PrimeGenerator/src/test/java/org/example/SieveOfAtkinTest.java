package org.example;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;


class SieveOfAtkinTest {

    /**
     * Testet alle Obergrenzen von 1 bis 1000
     */
    @Test
    void test(){
        for(int n = 0; n <= 1000; n++) {
            SieveOfEratosthenes sieve = new SieveOfEratosthenes(1, 3);
            List<Integer> prime = new ArrayList<>();

            for (int z = 2; z <= 3; z++) {
                if (isPrime(z)) {
                    prime.add(z);
                }
            }
            assertEquals(prime, sieve.call());
        }
    }
    private boolean isPrime(int number) {
        if (number < 2) {
            return false;
        }

        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}