# B. ICPC Balloons
# https://codeforces.com/problemset/problem/1703/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    print(n + len(set(s)))