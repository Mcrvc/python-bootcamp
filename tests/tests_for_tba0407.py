"""W2-4 Tests for tba0407's W1-4 (sieve of Eratosthenes)."""
from members.tba0407.w1.translate import primes_up_to

def test_small_n():
    assert primes_up_to(10) == [2, 3, 5, 7]


def test_two_is_first_prime():
    assert primes_up_to(2) == [2]


def test_zero_and_negative():
    assert primes_up_to(0) == []
    assert primes_up_to(-10) == []


def test_n_is_prime_itself():
    assert primes_up_to(13) == [2, 3, 5, 7, 11, 13]

def test_large_n():
    assert primes_up_to(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result = primes_up_to(1000)
    assert len(result) == 168 and result[-1] == 997