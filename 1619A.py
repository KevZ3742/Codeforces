# A. Square String?
# https://codeforces.com/problemset/problem/1619/A
# rating: 800

t = int(input())
 
for _ in range(t):
    s = input()

    if s[:len(s) // 2] == s[len(s) // 2:]:
        print("YES")
    else:
        print("NO")