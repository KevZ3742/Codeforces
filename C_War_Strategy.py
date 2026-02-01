# rating: ?

testCases = int(input())

for i in range(testCases):
    n, m, k = map(int, input().split())

    l = 0
    r = 0

    while True:
        tried = False

        if l < k - 1 and l + max(l + 1, r) + r <= m:
            l += 1
            tried = True
        
        if r < n - k and l + max(l, r + 1) + r <= m:
            r += 1
            tried = True
        
        if not tried:
            break

    print(l + r + 1)