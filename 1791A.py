# A. Codeforces Checking
# https://codeforces.com/problemset/problem/1791/A
# rating: 800

t = int(input())

for _ in range(t):
    c = input()

    if c in "codeforces":
        print("YES")
    else:
        print("NO")