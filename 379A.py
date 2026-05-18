# A. New Year Candles
# https://codeforces.com/problemset/problem/379/A
# rating: 1000

a, b = map(int, input().split())

toPrint = 0

while a > 0:
    toPrint += a
    a //= b

print(toPrint)