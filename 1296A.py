# A. Array with Odd Sum
# https://codeforces.com/problemset/problem/1296/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if sum(a) % 2:
        print("YES")
        continue

    evenExists = False
    oddExists = False

    for i in a:
        if i % 2:
            oddExists = True
        else:
            evenExists = True

    if evenExists and oddExists:
        print("YES")
    else:
        print("NO")