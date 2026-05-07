# A. One and Two
# https://codeforces.com/problemset/problem/1788/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    twoCount = a.count(2)
    if twoCount % 2:
        print(-1)
        continue

    target = twoCount // 2
    counter = 0
    for i, v in enumerate(a):
        if v == 2:
            counter += 1

        if counter == target:
            print(i + 1)
            break