# A. New Year and Hurry
# https://codeforces.com/problemset/problem/750/A
# rating: 800

n, k = map(int, input().split())

time = 240 - k
spend = 0
solved = 0

for i in range(1, n + 1):
    if spend + 5 * i > time:
        break
    spend += 5 * i
    solved += 1

print(solved)