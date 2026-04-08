# C. Turtle and Good Pairs
# https://codeforces.com/problemset/problem/2003/C
# rating: 1200

from collections import Counter, deque

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    counterS = Counter(s)

    a = sorted([(v, k) for k, v in counterS.items()], reverse=True)

    if len(a) == 1:
        print(s)
        continue
    
    toPrint = []
    while a[0][0] > a[1][0]:
        toPrint.append(a[0][1])
        a[0] = (a[0][0] - 1, a[0][1])

    q = deque(a)

    while q:
        count, char = q.popleft()
        if count == 0:
            continue

        toPrint.append(char)
        count -= 1
        q.append((count, char))

    print("".join(toPrint))