# A. Brain's Photos
# https://codeforces.com/problemset/problem/707/A
# rating: 800

n, m = map(int, input().split())

for _ in range(n):
    pixels = input().split()

    for item in pixels:
        if item not in ['B', 'W', 'G']:
            print("#Color")
            exit()
else:
    print("#Black&White")