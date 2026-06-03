# A. Robin Helps
# https://codeforces.com/problemset/problem/2014/A
# rating: 800

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    gold = 0
    ans = 0

    for x in a:
        if x >= k:
            gold += x
        elif x == 0 and gold > 0:
            gold -= 1
            ans += 1

    print(ans)