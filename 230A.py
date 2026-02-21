# A. Dragons
# https://codeforces.com/contest/230/problem/A
# rating: 1000

s, n = map(int, input().split())

dragons = []
for _ in range(n):
    x, y = map(int, input().split())

    dragons.append((x, y))

dragons.sort()

for dragon in dragons:
    if s > dragon[0]:
        s += dragon[1]
    else:
        print("NO")
        exit()

print("YES")