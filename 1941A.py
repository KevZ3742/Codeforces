# A. Rudolf and the Ticket
# https://codeforces.com/problemset/problem/1941/A
# rating: 800

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    count = 0

    for x in b:
        for y in c:
            if x + y <= k:
                count += 1

    print(count)