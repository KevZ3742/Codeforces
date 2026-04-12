# B. Make Almost Equal With Mod
# https://codeforces.com/problemset/problem/1909/B
# rating: 1200

t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(1, 60):
        bit = a[0] & 1

        if all((n & 1) == bit for n in a):
            a = [n >> 1 for n in a]
            continue

        print(2 ** i)
        break