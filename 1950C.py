# C. Clock Conversion
# https://codeforces.com/problemset/problem/1950/C
# rating: 800

t = int(input())

for _ in range(t):
    h, m = map(int, input().split(":"))

    newH = str(h % 12)

    if newH == "0":
        newH = "12"

    newM = str(m)

    if len(newH) == 1:
        newH = "0" + newH

    if len(newM) == 1:
        newM = "0" + newM

    toPrint = newH + ":" + newM

    if h > 11:
        toPrint += " PM"
    else:
        toPrint += " AM"

    print(toPrint)