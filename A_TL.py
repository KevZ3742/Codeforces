# rating: 1200

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

if a[-1] >= b[0]:
    print(-1)
    exit()

if a[0] * 2 > b[0] - 1:
    print(-1)
elif a[0] * 2 <= a[-1]:
    print(a[-1])
else:
    print(a[0] * 2)
