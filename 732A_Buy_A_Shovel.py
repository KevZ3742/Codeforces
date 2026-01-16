# https://codeforces.com/contest/732/problem/A
# rating: 800

k, r = map(int, input().split())

shovelCount = 1
while shovelCount * k % 10 != r:
    if shovelCount * k % 10 == 0:
        break
    shovelCount += 1

print(shovelCount)