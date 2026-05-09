# A. Laptops
# https://codeforces.com/problemset/problem/456/A
# rating: 1100

n = int(input())

arr = []

for _ in range(n):
    a, b = map(int, input().split())

    arr.append((a, b))

arr.sort()

for i in range(1, n):
    if arr[i][1] < arr[i - 1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")