# A. Only Pluses
# https://codeforces.com/problemset/problem/1992/A
# rating: 800

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    for i in range(5):
        if a <= b and a <= c:
            a += 1
        elif b <= a and b <= c:
            b += 1
        else:
            c += 1

    print(a * b * c)