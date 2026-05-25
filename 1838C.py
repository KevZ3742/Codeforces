# C. No Prime Differences
# https://codeforces.com/problemset/problem/1838/C
# rating: 1400

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    toPrint = [[]] * n
    counter = 1
    for i in range(1, n, 2):
        toPrint[i] = [*range(counter, counter + m)]
        counter += m

    for i in range(0, n, 2):
        toPrint[i] = [*range(counter, counter + m)]
        counter += m

    for i in toPrint:
        print(*i)