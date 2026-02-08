# rating: 1100

from collections import Counter

n = int(input())
w = Counter(map(int, input().split()))

if w[200] % 2 == 0:
    if w[100] % 2 == 0:
        print("YES")
    else:
        print("NO")
else:
    if w[100] % 2 == 0 and w[100] >= 2:
        print("YES")
    else:
        print("NO")