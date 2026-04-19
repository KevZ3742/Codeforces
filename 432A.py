# A. Choosing Teams
# https://codeforces.com/problemset/problem/432/A
# rating: 800

n, k = map(int, input().split())
y = sorted(map(int, input().split()))

teams = 0
cur = 0
for student in y:
    if student  <= 5 - k:
        cur += 1
    else:
        break

    if cur == 3:
        teams += 1
        cur = 0

print(teams)