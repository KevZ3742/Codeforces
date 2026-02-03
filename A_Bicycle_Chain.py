# rating: 900

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

gears = 0
maxRatio = 0

for i in a:
    for j in b:
        if j % i == 0:
            ratio = j // i

            if ratio > maxRatio:
                maxRatio = ratio
                gears = 1
            elif  ratio == maxRatio:
                gears += 1

print(gears)