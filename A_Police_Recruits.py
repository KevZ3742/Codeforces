# rating: 800

n = int(input())
a = list(map(int, input().split()))

cops = 0
crimes = 0
for i in a:
    if i > 0:
        cops += i
    else:
        if cops == 0:
            crimes += 1
        else:
            cops -= 1

print(crimes)