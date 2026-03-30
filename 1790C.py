# C. Premutation
# https://codeforces.com/problemset/problem/1790/C
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())

    seen = {}
    repeated = None

    for _ in range(n):
        a = list(map(int, input().split()))
        key = a[0]

        if key in seen:
            repeated = key
            seen[key] = None
        else:
            seen[key] = a

    unique = next(v for v in seen.values() if v is not None)
    print(repeated, *unique)