# B. Array merging
# https://codeforces.com/problemset/problem/1831/B
# rating: 1000

from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    aDic = defaultdict(int)
    bDic = defaultdict(int)

    prev = None
    currLength = 0
    for num in a:
        if prev is None or prev == num:
            currLength += 1
        else:
            aDic[prev] = max(aDic[prev], currLength)
            currLength = 1
        prev = num
    if prev is not None:
        aDic[prev] = max(aDic[prev], currLength)

    prev = None
    currLength = 0
    for num in b:
        if prev is None or prev == num:
            currLength += 1
        else:
            bDic[prev] = max(bDic[prev], currLength)
            currLength = 1
        prev = num
    if prev is not None:
        bDic[prev] = max(bDic[prev], currLength)

    sums = []

    allKey = set(aDic) | set(bDic)
    sums = [aDic[k] + bDic[k] for k in allKey]

    print(max(sums))