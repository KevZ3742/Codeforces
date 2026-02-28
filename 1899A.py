# A. Game with Integers
# https://codeforces.com/problemset/problem/1899/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())

    if n % 3:
        print("First")
    else:
        print("Second")