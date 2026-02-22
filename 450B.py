# B. Jzzhu and Sequences
# https://codeforces.com/problemset/problem/450/B
# rating: 1300

x, y = map(int, input().split())
n = int(input())

mod = 1000000007

toPrint = [x, y, y - x, -x, -y, x - y]

print(toPrint[(n-1) % 6] % mod)