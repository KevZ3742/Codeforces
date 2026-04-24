# B. Informatics in MAC
# https://codeforces.com/problemset/problem/1935/B
# rating: 1200

t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    rightArr = [0] * (n + 1)
    for i in a:
        rightArr[i] += 1

    rightMex = 0
    while rightArr[rightMex]:
        rightMex += 1

    leftArr = [0] * (n + 1)
    leftMex = 0

    for i in range(n):
        rightArr[a[i]] -= 1
        if rightArr[a[i]] == 0 and rightMex > a[i]:
            rightMex = a[i]

        leftArr[a[i]] += 1
        while leftArr[leftMex]:
            leftMex += 1

        if leftMex == rightMex:
            print(2)
            print(1, i + 1)
            print(i + 2, n)
            break
    else:
        print(-1)
    