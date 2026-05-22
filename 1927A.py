# A. Make it White
# https://codeforces.com/problemset/problem/1927/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    print(s.rfind("B") - s.find("B") + 1)