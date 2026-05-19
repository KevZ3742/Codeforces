# B. Make AP
# https://codeforces.com/problemset/problem/1624/B
# rating: 900

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    ok = False

    x = 2 * b - c
    if x > 0 and x % a == 0:
        ok = True

    x = a + c
    if x % (2 * b) == 0:
        ok = True

    x = 2 * b - a
    if x > 0 and x % c == 0:
        ok = True

    print("YES" if ok else "NO")