# B. Permutations & Primes
# https://codeforces.com/problemset/problem/1844/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(1)
        continue

    if n == 2:
        print(2, 1)
        continue

    toPrint = [0] * n
    toPrint[n // 2] = 1
    toPrint[0] = 2
    toPrint[-1] = 3

    counter = 4
    for i in range(n):
        if toPrint[i] == 0:
            toPrint[i] = counter
            counter += 1

    print(*toPrint)