# https://codeforces.com/problemset/problem/71/A

count = int(input())

words = []

for i in range(count):
    word = str(input())
    words.append(word)

for n in words:
    if len(n) > 10:
        toPrint = n[0] + str(len(n[1:-1])) + n[-1]
        print(toPrint)
    else:
        print(n)
