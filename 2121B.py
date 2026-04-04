# B. Above the Clouds
# https://codeforces.com/problemset/problem/2121/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    if s[0] in s[1:-1] or s[-1] in s[1:-1] or len(set(s[1:-1])) != len(s[1:-1]):
        print("Yes")
    else:
        print("No")