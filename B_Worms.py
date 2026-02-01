# https://codeforces.com/problemset/problem/474/B
# rating: 1200

n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

sumA = a
sum = 0
for _ in range(n):
    sum += a[_]
    sumA[_] = sum

for tag in q:
    l, r = 0, n - 1
    toPrint = r

    while l <= r:
        m = (l + r) // 2

        if sumA[m] >= tag:
            toPrint = m
            r = m - 1
        else:
            l = m + 1
        
    print(toPrint + 1)