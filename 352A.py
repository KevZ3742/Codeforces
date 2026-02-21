# A. Jeff and Digits
# https://codeforces.com/contest/352/problem/A
# rating: 1000

n = int(input())
a = list(map(int, input().split()))

count0 = a.count(0)
count5 = a.count(5)

if count0 == 0:
    print(-1)
else:
    max5 = count5 // 9 * 9

    if max5 == 0:
        print(0)
    else: 
        print("5" * max5  + "0" * count0)