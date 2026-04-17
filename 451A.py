# A. Game With Sticks
# https://codeforces.com/problemset/problem/451/A
# rating: 900

n, m = map(int, input().split())

if min(n, m) % 2 == 0:
    print("Malvika")
else:
    print("Akshat")