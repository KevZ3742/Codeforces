# B. The Curse of the Frog
# https://codeforces.com/problemset/problem/2189/B
# rating: 1200

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    jumps = []
    for i in range(n):
        a, b, c = map(int, input().split())
        jumps.append((a,b,c))

    distance = 0
    valuePerRollback = [0] * n

    for i in range(n):
        distance += jumps[i][0] * (jumps[i][1] - 1)
        valuePerRollback[i] = -jumps[i][2] + jumps[i][0] + jumps[i][0] * (jumps[i][1] - 1)

    if distance >= x:
        print(0)
        continue

    bestValue = max(valuePerRollback)

    if bestValue <= 0:
        print(-1)
        continue

    print(-(-(x - distance) // max(valuePerRollback)))