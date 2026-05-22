# A. Odd Set
# https://codeforces.com/problemset/problem/1542/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    numOdds = 0
    numEvens = 0

    for i in a:
        if i % 2:
            numOdds += 1
        else:
            numEvens += 1

    if numEvens == numOdds:
        print("Yes")
    else:
        print("No")