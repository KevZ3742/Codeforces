# A. Do Not Be Distracted!
# https://codeforces.com/problemset/problem/1520/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    seen = set()
    seen.add(s[0])
    prev = s[0]

    for i in range(1, n):
        if s[i] == prev:
            continue
        
        if s[i] in seen:
            print("NO")
            break

        seen.add(s[i])
        prev = s[i]
    else:
        print("YES")