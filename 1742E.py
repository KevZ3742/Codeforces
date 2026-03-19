# E. Scuza
# https://codeforces.com/problemset/problem/1742/E
# rating: 1200

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = list(map(int, input().split()))

    prefixSum = []
    curSum = 0
    for num in a:
        curSum += num
        prefixSum.append(curSum)

    prefixMax = []
    curMax = float("-inf")
    for num in a:
        curMax = max(curMax, num)
        prefixMax.append(curMax)
        
    toPrint = []
    for height in k:
        index = -1
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2

            if prefixMax[m] <= height:
                index = m
                l = m + 1
            else:
                r = m - 1

        if index == -1:
            toPrint.append(0)
        else:
            toPrint.append(prefixSum[index])

    print(*toPrint)

