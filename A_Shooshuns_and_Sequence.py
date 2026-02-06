# rating: 1200

n, k = map(int, input().split())
a = list(map(int, input().split()))

substr = a[k - 1:]
substrIsAllSame = len(set(substr)) == 1

if substrIsAllSame:
    subArrLen = 0
    value = a[-1]
    for i in range(n - 1, -1, -1):
        if a[i] != value:
            break
        else:
            subArrLen += 1
        
    print(n - subArrLen)
else:
    print(-1)