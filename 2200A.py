# A. Eating Game
# https://codeforces.com/contest/2200/problem/A
# rating: ?

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    maxDishes = max(a)
    print(a.count(maxDishes))