# A. Divisible Permutation
# https://codeforces.com/problemset/problem/2188/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())

    toPrint = [1, n]
    used = {1, n}
    for i in range(n - 2, 0, -1):
        prev = toPrint[-1]
        if 1 <= prev - i <= n and prev - i not in used:
            toPrint.append(prev - i)
            used.add(prev - i)
        else:
            toPrint.append(prev + i)
            used.add(prev + i)

    toPrint.reverse()
    print(*toPrint)
