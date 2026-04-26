# B. Even Array
# https://codeforces.com/problemset/problem/1367/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    toPrint = 0
    evens = 0
    odds = 0
    for i in range(n):
        if a[i] % 2 != i % 2:
            if i % 2:
                odds += 1
            else:
                evens += 1
                
        if odds > 0 and evens > 0:
            odds -= 1
            evens -= 1
            toPrint += 1

    if odds != 0 or evens != 0:
        print(-1)
    else:
        print(toPrint)
