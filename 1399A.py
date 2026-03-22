# A. Remove Smallest
# https://codeforces.com/problemset/problem/1399/A
# rating: 800

t = int(input())
 
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))

    if n == 1:
        print("YES")
        continue

    prev = a[0]
    for i in range(1, n):
        if a[i] > prev + 1:
            print("NO")
            break

        prev = a[i] 
    else:
        print("YES")