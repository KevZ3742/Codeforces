# C. Training Before the Olympiad
# https://codeforces.com/problemset/problem/1916/C
# rating: 1200

def pattern(n):
    group = n // 3
    position = n % 3

    if position == 1:
        return group + 1
    
    return group

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    oddCount = 0
    curSum = 0
    toPrint = []
    for i in range(n):
        curSum += a[i]

        if a[i] % 2:
            oddCount += 1

        if i == 0:
            toPrint.append(curSum)
            continue

        toPrint.append(curSum - pattern(oddCount))

    print(*toPrint)