import math

def primeFactorization(n):
    """
    Computes the prime factorization of an integer n.

    The algorithm repeatedly divides n by the smallest possible prime factor.
    It first removes all factors of 2, then checks odd numbers up to sqrt(n).
    Any remaining value greater than 2 is itself a prime factor.

    Args:
        n (int): The integer to factorize. Must be >= 2.

    Returns:
        list[int]: A list of the prime factors of n in non-decreasing order.
        Each prime factor appears as many times as it divides n.
    """

    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    return factors

# example usage
factors = primeFactorization(315)

print(factors)