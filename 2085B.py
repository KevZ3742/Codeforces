# B. Serval and Final MEX
# https://codeforces.com/problemset/problem/2085/B
# rating: 1200

def mex(arr):
    mex = 0

    while mex in arr:
        mex += 1
    
    return(mex)

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    operations = []

    l = a[:n // 2]
    r = a[n // 2:]

    if r.count(0) > 0:
        r = [mex(r)]
        operations.append((n // 2 + 1, n))
    
    if l.count(0) > 0:
        l = [mex(l)]
        operations.append((1, n // 2))

    operations.append((1, len(l + r)))

    print(len(operations))
    for operation in operations:
        print(*operation)