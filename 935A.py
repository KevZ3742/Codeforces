# A. Fafa and his Company
# https://codeforces.com/problemset/problem/935/A
# rating: 800

n = int(input())

divisors = 0

i = 1
while i * i <= n:
    if n % i == 0:
        divisors += 1
        if i != n // i:
            divisors += 1
    i += 1

print(divisors - 1)