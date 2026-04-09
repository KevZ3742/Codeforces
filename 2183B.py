# B. Yet Another MEX Problem
# https://codeforces.com/contest/2183/problem/B
# rating: 1100

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    mex = -1

    count = [0] * (n + 1)
    for i in a:
        count[i] += 1

    for i in range(k - 1):
        if not count[i]:
            mex = i
            break

    if mex == -1:
        mex = k - 1

    print(mex)