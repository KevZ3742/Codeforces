# B. Deletion Sort
# https://codeforces.com/contest/2200/problem/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if a == sorted(a):
        print(n)
        continue

    print(1)