# B. Keep it Beautiful
# https://codeforces.com/problemset/problem/1841/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())
    q = list(map(int, input().split()))

    increasing = True
    toPrint = []
    a = []
    for num in q:
        if not a:
            a.append(num)
            toPrint.append("1")
            continue

        if increasing:
            if num >= a[-1]:
                a.append(num)
                toPrint.append("1")
            elif num <= a[0]:
                increasing = False
                a.append(num)
                toPrint.append("1")
            else:
                toPrint += "0"
        else:
            if a[-1] <= num <= a[0]:
                a.append(num)
                toPrint.append("1")
            else:
                toPrint += "0"

    print("".join(toPrint))