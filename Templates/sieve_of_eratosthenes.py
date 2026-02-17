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
    for p in range(2, int(n ** .5) + 1):
        if isPrime[p]:
            primes.append(p)
        
            for i in range(p * p, n + 1, p):
                isPrime[i] = False
    
    return primes, isPrime

# example usage
primes, isPrime = sieveOfEratosthenes(100)

print(primes)
print(isPrime[97])