# rating: 1200

n = int(input())
a = list(map(int, input().split()))

ones = sum(a)

bestSubArr = -1
currentSubArr = 0

for i in a:
    if i == 0:
        value = 1
    else:
        value = -1

    currentSubArr = max(currentSubArr + value, value)
    bestSubArr = max(currentSubArr, bestSubArr)

print(ones + bestSubArr)