# C. Kefa and Park
# https://codeforces.com/problemset/problem/580/C
# rating: 1500

def addEdge(adj, i, j):
    adj[i].append(j)
    adj[j].append(i)

n, m = map(int, input().split())
a = list(map(int, input().split()))

adj = [[] for _ in range(n + 1)]

for i in range(n - 1):
    u, v = map(int, input().split())
    addEdge(adj, u, v)

toPrint = 0
stack = [[1, -1, 0]]

while stack:
    node, parent, cons = stack.pop()

    if a[node - 1] == 1:
        cons += 1
    else:
        cons = 0

    if cons > m:
        continue
    
    leaf = True

    for i in adj[node]:
        if i != parent:
            leaf = False
            stack.append([i, node, cons])

    if leaf:
        toPrint += 1

print(toPrint)