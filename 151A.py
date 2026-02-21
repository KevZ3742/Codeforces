# A. Soft Drinking
# https://codeforces.com/contest/151/problem/A
# rating: 800

n, k, l, c, d, p, nl, np = map(int, input().split())

ml = k * l // nl
limes = c * d
salt = p // np

print(min(ml, limes, salt) // n)