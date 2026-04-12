# A. Adjacent Digit Sums
# https://codeforces.com/problemset/problem/2067/A
# rating: 800

t = int(input())
 
for _ in range(t):
    x, y = map(int, input().split())

    if x + 1 - y >= 0 and (x + 1 - y) % 9 == 0:
        print("Yes")
        continue

    print("No")