# A. Short Substrings
# https://codeforces.com/problemset/problem/1367/A
# rating: 800

t = int(input())

for _ in range(t):
    b = input()

    toPrint = b[0]
    for i in range(1, len(b), 2):
        toPrint += b[i]

    print(toPrint)