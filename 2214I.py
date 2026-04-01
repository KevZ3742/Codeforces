# I. You Are a Robot
# https://codeforces.com/contest/2214/problem/I

t = int(input())

for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
        continue
        
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))

    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        parent = p[i]
        child = i + 2
        edge_type = a[i]
        adj[parent].append((child, edge_type))

    INF = (float('inf'), float('inf'))
    dp = [INF] * (n + 1)

    for i in range(n, 0, -1):
        if not adj[i]:
            dp[i] = (0, 0)
        else:
            best_choice = INF
            for child, edge_type in adj[i]:
                h, r = dp[child]
                if edge_type == 1:
                    h += 1
                elif edge_type == 2:
                    r += 1
                
                if (h, r) < best_choice:
                    best_choice = (h, r)
            dp[i] = best_choice

    curr = 1
    while adj[curr]:
        target = dp[curr]
        for child, edge_type in adj[curr]:
            h, r = dp[child]
            if edge_type == 1:
                h += 1
            elif edge_type == 2:
                r += 1
            
            if (h, r) == target:
                curr = child
                break
    
    print(curr)