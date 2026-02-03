# rating: 1000

from collections import Counter

k = int(input())
s = Counter(input())

toPrint = ""
for key in s.keys():
    if s[key] % k != 0:
        print(-1)
        exit()

    copies = s[key] // k
    toPrint += key * copies

print(toPrint * k)