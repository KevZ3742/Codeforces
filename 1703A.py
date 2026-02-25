# A. YES or YES?
# https://codeforces.com/problemset/problem/1703/A
# rating: 800

t = int(input())

for _ in range(t):
    s = input().lower()
    if s == "yes":
        print("YES")
    else:
        print("NO")