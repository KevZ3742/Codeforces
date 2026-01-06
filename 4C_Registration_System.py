# https://codeforces.com/problemset/problem/4/C
# rating: 1300

count = int(input())

names = {}

for i in range(count):
    name = input()
    names[name] = names.get(name, 0) + 1
    
    if names[name] == 1:
        print("OK")
    else:
        print(name + str(names[name] - 1))