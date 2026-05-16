# C. Word on the Paper
# https://codeforces.com/problemset/problem/1850/C
# rating: 800

t = int(input())

for _ in range(t):
    toPrint = []

    for i in range(8):
        s = input()
        s = s.replace(".", "")
        toPrint.append(s)

    print("".join(toPrint))