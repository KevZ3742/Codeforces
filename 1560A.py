# A. Dislike of Threes
# https://codeforces.com/problemset/problem/1560/A
# rating: 800

t = int(input())

for _ in range(t):
    k = int(input())

    counter = 0
    toPrint = 0

    while counter < k:
        toPrint += 1

        if toPrint % 3 == 0 or str(toPrint)[-1] == "3":
            continue

        counter += 1

    print(toPrint)