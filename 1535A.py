# A. Fair Playoff
# https://codeforces.com/problemset/problem/1535/A
# rating: 800

t = int(input())

for _ in range(t):
    players = list(map(int, input().split()))

    sortedPlayers = sorted(players)

    if (sortedPlayers[-1] in players[:2] and sortedPlayers[-2] in players[2:]) or (sortedPlayers[-2] in players[:2] and sortedPlayers[-1] in players[2:]):
        print("YES")
    else:
        print("NO")

