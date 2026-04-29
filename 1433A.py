# A. Boring Apartments
# https://codeforces.com/problemset/problem/1433/A
# rating: 800

t = int(input())

for _ in range(t):
    x = input()

    target = x[0]
    count = len(x)

    toPrint = 10 * (int(target) - 1)

    for i in range(1, count + 1):
        toPrint += i

    print(toPrint)
