# B. Normal Problem
# https://codeforces.com/problemset/problem/2044/B
# rating: 800

t = int(input())

for _ in range(t):
    a = list(input())
    a = a[::-1]

    for i in range(len(a)):
        if a[i] == "p":
            a[i] = "q"
        elif a[i] == "q":
            a[i] = "p"

    print("".join(a))