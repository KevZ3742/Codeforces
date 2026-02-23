# A. Adding Digits
# https://codeforces.com/problemset/problem/260/A
# rating: 1400

a, b, n = map(int, input().split())

toPrint = -1
for i in range(10):
    if (a * 10 + i) % b == 0:
        toPrint = (a * 10 + i)
        break

if toPrint == -1:
    print(toPrint)
else:
    print(str(toPrint) + "0" * (n - 1))