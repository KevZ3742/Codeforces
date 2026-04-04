# C. The 67th Permutation Problem
# https://codeforces.com/contest/2218/problem/C
# rating: ?

t = int(input())

for _ in range(t):
    n = int(input())

    toPrint = []
    l = 1
    h = 3 * n
    for i in range(n):
        temp = [l, h, h - 1]
        toPrint.extend(temp)

        l += 1
        h -= 2

    print(*toPrint)