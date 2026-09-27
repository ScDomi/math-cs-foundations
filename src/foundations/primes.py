from __future__ import annotations

import math


def is_prime_trial(n: int) -> bool:
    """Deterministic trial-division primality test using the sqrt(n) bound."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    for divisor in range(3, limit + 1, 2):
        if n % divisor == 0:
            return False
    return True


def primes_trial(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1) if is_prime_trial(n)]


def sieve_eratosthenes(limit: int) -> list[int]:
    """Return all primes <= limit with the classic O(n log log n) sieve."""
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [i for i, prime in enumerate(sieve) if prime]


def sieve_atkin(limit: int) -> list[int]:
    """Return all primes <= limit using the Sieve of Atkin.

    Kept here because the original PrimeGenerator explored Eratosthenes vs Atkin.
    For small limits Eratosthenes often wins due to lower constant overhead; Atkin is
    interesting mathematically because it flips entries based on quadratic forms.
    """
    if limit < 2:
        return []
    sieve = [False] * (limit + 1)
    root = math.isqrt(limit)
    for x in range(1, root + 1):
        for y in range(1, root + 1):
            n = 4 * x * x + y * y
            if n <= limit and n % 12 in (1, 5):
                sieve[n] = not sieve[n]
            n = 3 * x * x + y * y
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x * x - y * y
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    for n in range(5, root + 1):
        if sieve[n]:
            square = n * n
            for k in range(square, limit + 1, square):
                sieve[k] = False
    primes = [2, 3]
    primes.extend(n for n in range(5, limit + 1) if sieve[n])
    return [p for p in primes if p <= limit]


def miller_rabin(n: int) -> bool:
    """Deterministic Miller-Rabin for 64-bit integers."""
    if n < 2:
        return False
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if n in small:
        return True
    if any(n % p == 0 for p in small):
        return False
    d, s = n - 1, 0
    while d % 2 == 0:
        s += 1
        d //= 2
    # Valid for n < 2^64
    for a in [2, 3, 5, 7, 11, 13, 17]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
