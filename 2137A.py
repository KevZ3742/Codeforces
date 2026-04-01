# A. Collatz Conjecture
# https://codeforces.com/problemset/problem/2137/A
# rating: 800

t = int(input())

for _ in range(t):
    k, x = map(int, input().split())

    print(x * 2 ** k)