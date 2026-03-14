# B. Shohag Loves Strings
# https://codeforces.com/problemset/problem/2039/B
# rating: 1000

t = int(input())

for _ in range(t):
    s = input()

    if len(s) == 1:
        print(-1)
        continue

    prev2 = s[0]
    prev = s[1]

    if prev == prev2:
        print(prev + prev)
        continue

    for i in range(2, len(s)):
        if s[i] == prev:
            print(prev + prev)
            break
        
        if prev2 != prev and prev != s[i] and prev2 != s[i]:
            print(prev2 + prev + s[i])
            break

        prev2 = prev
        prev = s[i]
    else:
        print(-1)