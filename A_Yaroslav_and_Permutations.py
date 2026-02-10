# rating: 1100

from collections import Counter
import math

n = int(input())
a = list(map(int, input().split()))
counterA = Counter(a)

if max(counterA.values()) <= math.ceil(n / 2):
    print("YES")
else:
    print("NO")