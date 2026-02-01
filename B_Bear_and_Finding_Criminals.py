# https://codeforces.com/contest/680/problem/B
# rating: 1000

n, a = map(int, input().split())
t = list(map(int, input().split()))
a -= 1

arrests = 0
for i in range(max(n - a, a + 1) + 1):
    cityCount = 0
    criminalCount = 0

    if i > 0:
        if a - i >= 0:
            cityCount += 1
            criminalCount += t[a - i]

        if a + i <= n - 1:
            cityCount += 1
            criminalCount += t[a + i]
    else:
        if t[a] == 1:
            criminalCount = 1

    if criminalCount == 1:
        if i == 0:
            arrests += 1
        elif cityCount == 1:
            arrests += 1
    
    if criminalCount == 2:
        arrests += 2

print(arrests)