# A. Gravity Flip
# https://codeforces.com/contest/405/problem/A
# rating: 900

n = int(input())
a = list(map(int, input().split()))

a.sort()

print(' '.join(map(str, a)))