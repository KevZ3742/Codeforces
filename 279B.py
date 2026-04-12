# B. Books
# https://codeforces.com/contest/279/problem/B
# rating: 1400

n, t = map(int, input().split())
a = list(map(int, input().split()))

l = 0
maxBooks = 0
minutes = 0

for r in range(n):
    minutes += a[r]

    while minutes > t:
        minutes -= a[l]
        l += 1
    
    maxBooks = max(maxBooks, r - l + 1)

print(maxBooks)