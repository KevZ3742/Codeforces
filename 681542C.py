# C. Double Sort
# https://codeforces.com/gym/681542/problem/C

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if a == b == sorted(a):
        print(0)
        continue

    ab = list(zip(a, b))
    ab.sort(key=lambda x: (x[0], x[1]))

    newA, newB = zip(*ab)
    
    if list(newA) == sorted(a) and list(newB) == sorted(b):
        toPrint = []

        for i in range(n):
            for j in range(i, n):
                if (a[j], b[j]) == ab[i]:
                    swap = j
                    break

            if swap == i:
                continue

            a[i], a[swap] = a[swap], a[i]
            b[i], b[swap] = b[swap], b[i]

            toPrint.append((i + 1, swap + 1))
    else:
        print(-1)
        continue

    print(len(toPrint))
    for i in toPrint:
        print(*i)