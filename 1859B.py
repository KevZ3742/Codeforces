# B. Olya and Game with Arrays
# https://codeforces.com/problemset/problem/1859/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())

    toPrint = []
    smallest = float("inf")

    for i in range(n):
        m = int(input())
        a = list(map(int, input().split()))

        a.sort()

        temp = min(smallest, a[0])
        if temp != smallest:
            smallest = temp

        toPrint.append(a[1])

    print(sum(toPrint) - min(toPrint) + smallest)
        