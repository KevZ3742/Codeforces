# rating: 1200

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    counter = 0
    mapp = {}
    for i in range(n):
        key = a[i] - i
        counter += mapp.get(key, 0)
        mapp[key] = mapp.get(key, 0) + 1

    print(counter)