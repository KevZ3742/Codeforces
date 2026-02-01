# rating: 900

import math

n = int(input())
s = list(input())
s = s[::-1]

decoded = [""] * n

for i in range(n):
    curr = 0
    if i % 2 == 0:
        curr = n - 1 - i // 2
    else:
        curr = i // 2

    decoded[curr] = s[i]

print(''.join(decoded))