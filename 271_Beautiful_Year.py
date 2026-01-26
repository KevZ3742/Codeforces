# https://codeforces.com/problemset/problem/271/A
# rating: 800

y = int(input())

y += 1
while len(set(str(y))) < 4:
    y += 1

print(y)