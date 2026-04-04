# A. Greedy Grid
# https://codeforces.com/problemset/problem/2122/A
# rating: 800

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    if (n == 1 or m == 1) or (n == m == 2):
        print("NO")
        continue

    print("YES")