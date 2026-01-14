# https://codeforces.com/contest/2183/problem/B
# rating: ?

testCases = int(input())

for i in range(testCases):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    mex = -1

    count = [0] * (n + 1)
    for _ in a:
        count[_] += 1

    for _ in range(k-1):
        if not count[_]:
            mex = _
            break

    if mex == -1:
        mex = k-1

    print(mex)