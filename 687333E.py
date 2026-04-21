# E. Exploding Houses
# https://codeforces.com/group/EW9LgKVDr6/contest/687333/problem/E

from collections import deque

def add_edge(adj, i, j):
    adj[i].append(j)
    adj[j].append(i)

n, m = map(int, input().split())

if m == 0:
    print(n)
    exit()

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    add_edge(adj, i, j)

color = [-1] * (n + 1)
toPrint = 0

for start in range(1, n + 1):
    if color[start] == -1:
        toPrint += 1
        q = deque([start])
        color[start] = 0

        while q:
            u = q.popleft()

            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    print(0)
                    exit()

print(toPrint)