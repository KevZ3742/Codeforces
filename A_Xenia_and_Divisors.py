# rating: 1200

from collections import Counter

n = int(input())
a = list(map(int, input().split()))

if len(set(a)) < 3:
    print(-1)
    exit()

if 5 in a or 7 in a:
    print(-1)
    exit()

a = Counter(a)
toPrint = []
while a[1] > 0 and a[3] > 0 and a[6] > 0:
    toPrint.append((1, 3, 6))
    a[1] -= 1
    a[3] -= 1
    a[6] -= 1

while a[1] > 0 and a[2] > 0 and a[6] > 0:
    toPrint.append((1, 2, 6))
    a[1] -= 1
    a[2] -= 1
    a[6] -= 1

while a[1] > 0 and a[2] > 0 and a[4] > 0:
    toPrint.append((1, 2, 4))
    a[1] -= 1
    a[2] -= 1
    a[4] -= 1

if len(toPrint) != n // 3:
    print(-1)
else:
    for i in toPrint:
        print(*i)