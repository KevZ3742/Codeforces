# rating: 1200

import math

n = int(input())

counter = 0
for a in range(1, n):
    for b in range(a + 1, n):
        c = math.sqrt(a * a + b * b)

        if int(c) == c and c <= n:
            counter += 1

print(counter)