# B. Paint a Strip
# https://codeforces.com/problemset/problem/2040/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())

    x = 1
    counter = 1
    while x < n:
        x = (x + 1) * 2
        counter += 1

    print(counter)