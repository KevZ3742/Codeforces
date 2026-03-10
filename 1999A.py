# A. A+B Again?
# https://codeforces.com/problemset/problem/1999/A
# rating: 800

t = int(input())

for _ in range(t):
    n = input()
    
    toPrint = 0
    for digit in n:
        toPrint += int(digit)

    print(toPrint)