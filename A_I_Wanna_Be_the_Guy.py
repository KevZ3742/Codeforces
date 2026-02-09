# rating: 800

n = int(input())
a = set(map(int, input().split()[1:]))
b = set(map(int, input().split()[1:]))

sett = a | b

if len(sett) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
