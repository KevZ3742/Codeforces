# D. Distinct Split
# https://codeforces.com/problemset/problem/1791/D
# rating: 1200

t = int(input())

for _ in range(t):
    n = int(input())
    a = input()

    prefix = [0] * n
    suffix = [0] * n

    prefixSet = set()
    suffixSet = set()
    for i in range(n):
        prefixSet.add(a[i])
        suffixSet.add(a[n - 1 - i])
        prefix[i] = len(prefixSet)
        suffix[n - 1 - i] = len(suffixSet)

    toPrint = -1
    for i in range(n - 1):
        toPrint = max(toPrint, prefix[i] + suffix[i + 1])

    print(toPrint)