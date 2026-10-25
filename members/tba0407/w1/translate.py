def primes_up_to(n: int) -> list[int]:
    """Find all primes up to ``n`` using the Sieve of Eratosthenes.

    Difference from C++:
    - In C++, fixed-size arrays or std::vector<bool> are typically pre-allocated.
      In Python, list repetition `[True] * (n + 1)` and dynamic list `.append()`
      are used to handle memory management automatically and more Pythonically.
    """
    if n < 2:
        return []

    is_prime = [True] * (n + 1)

    is_prime[0] = is_prime[1] = False

    for i in range(4, n + 1, 2):
        is_prime[i] = False

    p = 3
    while p * p <= n:
        if not is_prime[p]:
            p += 2
            continue

        for i in range(p * p, n + 1, 2 * p):
            is_prime[i] = False

        p += 2

    primes: list[int] = []
    for i in range(2, n + 1):
        if not is_prime[i]:
            continue

        primes.append(i)

    return primes
