# A. Vlad and the Best of Five
# https://codeforces.com/problemset/problem/1926/A
# rating: 800

t = int(input())

for _ in range(t):
    s = input()

    if s.count("A") > s.count("B"):
        print("A")
    else:
        print("B")