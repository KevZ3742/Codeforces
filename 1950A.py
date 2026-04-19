# A. Stair, Peak, or Neither?
# https://codeforces.com/problemset/problem/1950/A
# rating: 800

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    if b > a and b > c:
        print("PEAK")
    elif a < b < c:
        print("STAIR")
    else:
        print("NONE")