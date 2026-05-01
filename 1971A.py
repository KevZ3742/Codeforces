# A. My First Sorting Problem
# https://codeforces.com/problemset/problem/1971/A
# rating: 800

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    
    print(*sorted([x,y]))