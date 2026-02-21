# C. Shifted MEX
# https://codeforces.com/contest/2185/problem/C
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(set(map(int, input().split())))
    a.sort()

    substr = []
    for i in a:
        if i - 1 not in a:
            curr = i
            tempSubstr = []

        while curr in a:
            tempSubstr.append(curr)
            curr += 1
        
        if len(tempSubstr) > len(substr):
            substr = tempSubstr

    x = 0 - substr[0]

    for i in range(len(substr)):
        substr[i] += x

    mex = 0

    while mex in substr:
        mex += 1

    print(mex)