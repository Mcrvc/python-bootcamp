def sieve(n: int) -> list[int]:
    if n < 2: return []

    isPrime = [True]*(n + 1)

    isPrime[0] = isPrime[1] = False

    for i in range(4, n + 1, 2):
        isPrime[i] = False

    p = 3
    while p * p <= n:
        if not isPrime[p]: continue

        for i in range(p * p, n + 1, 2 * p):
            isPrime[i] = False

        p += 2


    primes = []
    for i in range(2, n + 1):
        if not isPrime[i]: continue

        primes.append(i)

    return primes
