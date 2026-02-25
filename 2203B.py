# B. Beautiful Numbers
# https://codeforces.com/contest/2203/problem/B
# rating: ?

t = int(input())

for _ in range(t):
    x = list(map(int, input()))
    s = sum(x)
    
    if s <= 9:
        print(0)
        continue

    x[0] -= 1
    sortedX = sorted(x, reverse=True)

    toPrint = 0
    currSum = s
    for digit in sortedX:
        if currSum <= 9:
            break

        currSum -= digit
        toPrint += 1

    print(toPrint)