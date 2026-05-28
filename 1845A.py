# A. Forbidden Integer
# https://codeforces.com/problemset/problem/1845/A
# rating: 800

t = int(input())

for _ in range(t):
    n, k, x = map(int, input().split())

    if x != 1:
        print ("YES")
        print(n)
        print("1 " * n)
    elif k == 2 and n % 2 == 0:
        print("YES")
        print(n // 2)
        print("2 " * (n // 2))
    elif n == 1:
        print("NO")
    elif k >= 3:
        print("YES")
        print(n // 2)
        if n % 2:
            print("2 " * (n // 2 - 1) + "3")
        else:
            print("2 " * (n // 2))
    else:
        print("NO")