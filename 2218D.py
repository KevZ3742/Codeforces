# D. The 67th OEIS Problem
# https://codeforces.com/contest/2218/problem/D
# rating: 800

def sieveOfEratosthenes(n: int):
    """
    Computes all prime numbers up to n using the Sieve of Eratosthenes.

    The sieve works by iteratively marking the multiples of each prime number
    starting from 2. Any number that remains unmarked is prime.

    Args:
        n (int): The inclusive upper bound. Finds all primes in range [2, n].

    Returns:
        tuple: A tuple containing:
            - primes (list[int]): All prime numbers <= n in ascending order.
            - isPrime (list[bool]): Boolean list of length n+1 where isPrime[x]
              is True if x is prime, False otherwise.
    """

    primes = []
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False

    for p in range(2, int(n ** .5) + 1):
        if isPrime[p]:
            for i in range(p * p, n + 1, p):
                isPrime[i] = False

    for p in range(2, n + 1):
        if isPrime[p]:
            primes.append(p)
    
    return primes, isPrime

primes, _ = sieveOfEratosthenes(10 ** 6)

t = int(input())

for _ in range(t):
    n = int(input())

    toPrint = [primes[0]]
    for i in range(1, n):
        toPrint.append(primes[i - 1] * primes[i])

    print(*toPrint)