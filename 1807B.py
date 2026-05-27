# B. Grab the Candies
# https://codeforces.com/problemset/problem/1807/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    even = sum(x for x in a if x % 2 == 0)
    odd = sum(x for x in a if x % 2 == 1)

    if even > odd:
        print("YES")
    else:
        print("NO")