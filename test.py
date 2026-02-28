t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    mid = a[x:y]
    minMid = min(mid)
    mid = mid[minMid:] + mid[:minMid]

    outer = a[:x] + a[y:]

    if len(outer) == 0:
        print(*mid)
        continue

    for i in range(len(outer)):
        if outer[i] > mid[0]:
            print(*(outer[:i] + mid + outer[i:]))
            continue