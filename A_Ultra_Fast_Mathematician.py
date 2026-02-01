# https://codeforces.com/problemset/problem/61/A
# rating: 800

a = str(input())
b = str(input())

toPrint = ""
for i in range(len(a)):
    if a[i] != b[i]:
        toPrint += "1"
    else:
        toPrint += "0"

print(toPrint)