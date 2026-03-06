# D. Replace with Occurrences
# https://codeforces.com/problemset/problem/2137/D
# rating: 1200

t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    count = [[] for i in range(n + 1)]
    for i in range(n):
        count[b[i]].append(i)

    flag = False
    for key in range(1, n + 1):
        if len(count[key]) % key != 0:
            flag = True
            break

    if flag:
        print(-1)
        continue

    a = [0] * n
    counter = 1
    for key in range(1, n + 1):
        limit = key
        temp = 0
        
        for i in count[key]:
            a[i] = counter
            temp += 1
            if temp == limit:
                temp = 0
                counter += 1

    print(*a)