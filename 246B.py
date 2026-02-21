# B. Increase and Decrease
# https://codeforces.com/contest/246/problem/B
# rating: 1300

n = int(input())
a = list(map(int, input().split()))

sumA = sum(a)

if sumA % n == 0:
    print(n)
else:
    print(n - 1)