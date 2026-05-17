# B. Ilya and Queries
# https://codeforces.com/problemset/problem/313/B
# rating: 1100

s = input()
m = int(input())

prefix = [0]
same = 0
prev = s[0]
for i in range(1, len(s)):
    if s[i] == prev:
        same += 1

    prefix.append(same)
    prev = s[i]

for _ in range(m):
    l, r = map(int, input().split())
    l -= 1
    r -= 1

    print(prefix[r] - prefix[l])