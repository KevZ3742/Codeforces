# B. Fair Division
# https://codeforces.com/problemset/problem/1472/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if sum(a) % 2:
        print("NO")
    else:
        target = sum(a) // 2
        if target % 2:
            print("YES" if a.count(1) > 0 else "NO")
        else:
            print("YES")        