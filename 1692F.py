# F. 3SUM
# https://codeforces.com/problemset/problem/1692/F
# rating: 1300

from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        a[i] %= 10

    counterA = Counter(a)

    digits = []
    for d in counterA:
        for i in range(min(3, counterA[d])):
            digits.append(d)

    found = False
    numDigits = len(digits)
    for i in range(numDigits):
        for j in range(i + 1, numDigits):
            for k in range(j + 1, numDigits):
                if (digits[i] + digits[j] + digits[k]) % 10 == 3:
                    found = True

    if found:
        print("YES")
    else:
        print("NO")