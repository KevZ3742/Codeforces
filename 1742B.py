# B. Increasing
# https://codeforces.com/problemset/problem/1742/B
# rating: 800

t = int(input()) 

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if sorted(a) == sorted(list(set(a))):
        print("YES")
    else:
        print("NO")