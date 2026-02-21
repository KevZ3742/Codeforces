# A. Twins
# https://codeforces.com/contest/160/problem/A
# rating: 900

count = int(input())
coins = list(map(int, input().split()))

coins.sort(reverse=True)

mySum = 0
myCoinCount = 0
total = sum(coins)

for n in coins:
    mySum += n
    total -= n
    myCoinCount += 1
    if mySum > total:
        break

print(myCoinCount)