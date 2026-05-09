# D. Odd Queries
# https://codeforces.com/problemset/problem/1807/D
# rating: 900

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    prefixSum = [0] * n
    prefixSum[0] = a[0]
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + a[i]

    suffix_sum = [0] * n
    suffix_sum[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + a[i]

    for i in range(q):
        l, r, k = map(int, input().split())
        l -= 1
        r -= 1

        left = prefixSum[l - 1] if l > 0 else 0
        right = suffix_sum[r + 1] if r < n - 1 else 0

        tot = left + right
        change = (r - l + 1) * k
        
        if (tot + change) % 2:
            print("YES")
        else:
            print("NO")