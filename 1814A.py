# A. Coins
# https://codeforces.com/problemset/problem/1814/A
# rating: 800

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    for x in range(2):
        if n - x * k >= 0 and (n - x * k) % 2 == 0:
            print("YES")
            break
    else:
        print("NO")