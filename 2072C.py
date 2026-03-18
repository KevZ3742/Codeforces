# C. Creating Keys for StORages Has Become My Main Skill
# https://codeforces.com/problemset/problem/2072/C
# rating: 1200

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    if n == 1:
        print(x)
        continue

    flag = True
    toPrint = [x] * n
    cur = 0
    for i in range(n - 1):
        if ((cur | i) & x) == (cur | i):
            cur |= i
            toPrint[i] = i
        else:
            flag = False
            break

    if flag and ((cur | (n - 1)) == x):
        toPrint[n - 1] = n - 1

    print(*toPrint)