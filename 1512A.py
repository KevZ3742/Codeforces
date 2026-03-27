# A. Spy Detected!
# https://codeforces.com/problemset/problem/1512/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    chars = list(set(a))

    if a.count(chars[0]) == 1:
        print(a.index(chars[0]) + 1)
    else:
        print(a.index(chars[1]) + 1)