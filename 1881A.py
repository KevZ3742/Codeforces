# A. Don't Try to Count
# https://codeforces.com/problemset/problem/1881/A
# rating: 800

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x = input()
    s = input()

    for i in range(6):
        if s in x:
            print(i)
            break

        x += x
    else:
        print(-1)