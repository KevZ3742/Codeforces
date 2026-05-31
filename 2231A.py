# A. Construct an Array
# https://codeforces.com/problemset/problem/2231/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())

    toPrint = [2 * i + 1 for i in range(n)]
    print(*toPrint)