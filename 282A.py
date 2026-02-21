# A. Bit++
# https://codeforces.com/contest/282/problem/A
# rating: 800

count = int(input())

x = 0

for i in range(count):
    statement = str(input())
    if "+" in statement:
        x+=1
    else:
        x-=1

print(x)