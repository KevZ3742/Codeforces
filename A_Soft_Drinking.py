# https://codeforces.com/problemset/problem/151/A
# rating: 800

n, k, l, c, d, p, nl, np = map(int, input().split())

ml = k * l // nl
limes = c * d
salt = p // np

print(min(ml, limes, salt) // n)