# A. Cards with Numbers
# https://codeforces.com/contest/254/problem/A
# rating: 1200

from collections import defaultdict

file = open("input.txt", "r")
output = open("output.txt", "w")

n = int(file.readline())
a = list(map(int, file.readline().split()))

cards = defaultdict(list)
for i in range(2 * n):
    cards[a[i]].append(i + 1)

toPrint = []
for key in cards.keys():
    if len(cards[key]) % 2 == 1:
        output.write("-1")
        exit()

    while cards[key]:
        toPrint.append([cards[key].pop(), cards[key].pop()])

for pair in toPrint:
    output.write(str(pair[0]) + " " + str(pair[1]) + "\n")