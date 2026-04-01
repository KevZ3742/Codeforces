# C. Best Binary String
# https://codeforces.com/problemset/problem/1837/C
# rating: 1000

t = int(input())

for _ in range(t):
    s = input()

    prev = "0"
    toPrint = []
    for c in s:
        if c == "?":
            toPrint.append(prev)
        else:
            toPrint.append(c)
            prev = c

    print("".join(toPrint))
