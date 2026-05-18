# A. New Year Candles
# https://codeforces.com/problemset/problem/379/A
# rating: 1000

a, b = map(int, input().split())

hours = 0
leftovers = 0

while a > 0:
    hours += a
    leftovers += a

    a = leftovers // b
    leftovers %= b

print(hours)