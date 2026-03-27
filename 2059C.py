# C. Customer Service
# https://codeforces.com/contest/2059/problem/C
# rating: 1600

t = int(input())

for _ in range(t):
    n = int(input())

    suffixOnes = []

    for i in range(n):
        a = list(map(int, input().split()))

        counter = 0
        for j in reversed(a):
            if j == 1:
                counter += 1
            else:
                break

        suffixOnes.append(counter)

    suffixOnes.sort()

    toPrint = 0
    for n in suffixOnes:
        if n >= toPrint:
            toPrint += 1

    print(toPrint)
