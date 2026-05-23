# B. Comparison String
# https://codeforces.com/problemset/problem/1837/B
# rating: 900

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    maxLen = 1
    prev = s[0]
    cur = 1
    for i in range(1, n):
        if s[i] == prev:
            cur += 1
        else:
            maxLen = max(maxLen, cur)
            cur = 1

        prev = s[i]

    maxLen = max(maxLen, cur)

    print(maxLen + 1)