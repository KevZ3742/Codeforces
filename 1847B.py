# B. Hamon Odyssey
# https://codeforces.com/problemset/problem/1847/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    fAll = a[0]
    for num in a[1:]:
        fAll &= num

    if fAll > 0:
        print(1)
    else:
        toPrint = 0
        f = -1

        for num in a:
            f &= num
            if f == 0:
                toPrint += 1
                f = -1

        print(toPrint)