# C. Replace and Sum
# https://codeforces.com/contest/2193/problem/C
# rating: 1000

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    curMax = max(a[-1], b[-1])
    for i in range(n - 1, -1, -1):
        curMax = max(a[i], b[i], curMax)
        a[i] = curMax

    prefSum  = [0] * (n + 1)
    for i in range(n):
        prefSum[i + 1] = prefSum[i] + a[i]

    ans = []
    for i in range(q):
        l, r = map(int, input().split())
        ans.append(prefSum[r] - prefSum[l - 1])
    
    print(*ans)