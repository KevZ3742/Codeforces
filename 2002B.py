# B. Removals Game
# https://codeforces.com/problemset/problem/2002/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if b == a or b == a[::-1]:
        print("Bob")
    else:
        print("Alice")