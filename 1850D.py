# D. Balanced Round
# https://codeforces.com/problemset/problem/1850/D
# rating: 900

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))

    prefixDiff = []
    prev = a[0]
    for i in range(1, n):
        prefixDiff.append(a[i] - prev)
        prev = a[i]

    

    maxLen = 0
    cur = 1
    for prefix in prefixDiff:
        if prefix > k:
            maxLen = max(maxLen, cur)
            cur = 1
        else:
            cur += 1
    
    maxLen = max(maxLen, cur)
    
    print(n - maxLen)