# B. Multiply by 2, divide by 6
# https://codeforces.com/problemset/problem/1374/B
# rating: 900

t = int(input())

for _ in range(t):
    n = int(input())

    toPrint = 0

    count2 = 0
    count3 = 0

    while n % 2 == 0:
        count2 += 1
        n //= 2

    while n % 3 == 0:
        count3 += 1
        n //= 3

    if n != 1 or count2 > count3:
        print(-1)
    else:
        print(2 * count3 - count2)