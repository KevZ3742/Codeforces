# A. Expression
# https://codeforces.com/contest/479/problem/A
# rating: 1000

a = int(input())
b = int(input())
c = int(input())

ans = max(a + b + c, (a + b) * c, a * (b + c), a * b * c)

print(ans)