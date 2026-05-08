# D. Alternating Path
# https://codeforces.com/problemset/problem/2204/D
# rating: 1400

from collections import deque

def add_edge(adj, i, j):
    adj[i].append(j)
    adj[j].append(i)

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    adj = [[] for _ in range(n + 1)]

    for i in range(m):
        v, u = map(int, input().split())
        add_edge(adj, v, u)

    color = [-1] * (n + 1)
    toPrint = 0

    for start in range(1, n + 1):
        if color[start] == -1:
            q = deque([start])
            color[start] = 0
            counts = [1, 0]
            flag = True

            while q:
                u = q.popleft()

                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        counts[color[v]] += 1
                        q.append(v)
                    elif color[v] == color[u]:
                        flag = False
                        
            if flag:
                toPrint += max(counts[0], counts[1])

    print(toPrint)