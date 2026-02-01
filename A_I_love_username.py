# https://codeforces.com/problemset/problem/155/A
# rating: 800

n = int(input())
p = list(map(int, input().split()))

minPoints = p[0]
maxPoints = p[0]

amazingPerformances = 0
for i in range(1, n):
    if minPoints > p[i]:
        amazingPerformances += 1
        minPoints = p[i]

    if maxPoints < p[i]:
        amazingPerformances += 1
        maxPoints = p[i]

print(amazingPerformances)