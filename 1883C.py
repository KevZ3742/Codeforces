# C. Raspberries
# https://codeforces.com/problemset/problem/1883/C
# rating: 1000

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    modArr = [num % k for num in a]

    if k == 4:
        evens = sum(num % 2 == 0 for num in a)

        if 0 in modArr:
            print(0)
            continue
        if evens >= 2:
            print(0)
            continue
        if evens == 1:
            print(1)
            continue
        
        print(min(k - max(modArr), 2))    
    else:

        if 0 in modArr:
            print(0)
            continue

        print(k - max(modArr))