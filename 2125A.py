# A. Difficult Contest
# https://codeforces.com/problemset/problem/2125/A
# rating: 800

t = int(input())

for _ in range(t):
    s = list(input())

    s.sort(reverse=True)

    print("".join(s))