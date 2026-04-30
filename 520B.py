# B. Two Buttons
# https://codeforces.com/problemset/problem/520/B
# rating: 1400

n, m = map(int, input().split())

counter = n
while m > n:
    if m % 2:
        m += 1
    else:
        m //= 2

    counter += 1

print(counter - m)