# D. Blackslex and Penguin Civilization
# https://codeforces.com/problemset/problem/2179/D
# rating: 1300

t = int(input())

for _ in range(t):
    n = int(input())

    target = 2 ** n - 1

    used = [False] * 2 ** n
    toPrint = [target, target >> 1]

    used[target] = True
    target >>= 1
    used[target] = True
    target >>= 1

    counter = 1
    multiplier = n - 1

    while multiplier >= 2:
        toPrint.append(target)
        used[target] = True

        while target + (counter * 2 ** multiplier) < 2 ** n - 1:
            toPrint.append(target + (counter * 2 ** multiplier))
            used[target + (counter * 2 ** multiplier)] = True
            counter += 1

        target >>= 1
        multiplier -= 1
        counter = 1

    for i in range(2 ** n):
        if not used[i]:
            toPrint.append(i)

    print(*toPrint)