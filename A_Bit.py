# https://codeforces.com/problemset/problem/282/A
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