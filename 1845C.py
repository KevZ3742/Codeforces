# C. Strong Password
# https://codeforces.com/problemset/problem/1845/C
# rating: 1400

t = int(input())

for _ in range(t):
    s = input()
    m = int(input())
    l = input()
    r = input()

    nextPos = [[-1] * 10 for _ in range(len(s) + 1)]

    for i in range(len(s) - 1, -1, -1):
        for j in range(10):
            nextPos[i][j] = nextPos[i + 1][j]

        digit = int(s[i])
        nextPos[i][digit] = i

    cur = 0
    isPossible = False
    for i in range(m):
        farthest = -1
        for j in range(int(l[i]), int(r[i]) + 1):
            next = nextPos[cur][j]

            if next == -1:
                isPossible = True
                break

            farthest = max(farthest, next)

        if isPossible:
            break

        cur = farthest + 1

    if isPossible:
        print("YES")
    else:
        print("NO")