# https://codeforces.com/problemset/problem/996/A
# rating: 800

balance = int(input())

bills = [100, 20, 10, 5, 1]

billCount = 0

for bill in bills:
    count = balance // bill
    billCount += count
    balance -= count * bill

print(billCount)