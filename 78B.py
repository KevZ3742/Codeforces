# B. Easter Eggs
# https://codeforces.com/contest/78/problem/B
# rating: 1200

n = int(input())

colors = "ROYGBIV"

noModificationRemainders = [0,4,5,6]

repetitions = n // 7
remainder = n % 7

toPrint = ""
if remainder in noModificationRemainders:
    toPrint = colors * repetitions + colors[:remainder]
else:
    toPrint = colors * repetitions + colors[3:3 + remainder]

print(toPrint)