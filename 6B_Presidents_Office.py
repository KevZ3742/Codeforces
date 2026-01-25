# https://codeforces.com/contest/6/problem/B
# rating: 1100

n, m, c = input().split()
n, m = int(n), int(m)

room = []
for _ in range(n):
    room.append(list(input()))

deputies = set()

# wip