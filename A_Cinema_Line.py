# rating: 1100

from collections import Counter

n = int(input())
a = list(map(int, input().split()))

counterA = Counter()

for bill in a:
    if bill == 25:
        counterA[25] += 1
    elif bill == 50:
        counterA[50] += 1
        if counterA[25] >= 1:
            counterA[25] -= 1
        else: 
            print("NO")
            exit()
    else:
        if counterA[50] >= 1 and counterA[25] >= 1:
            counterA[50] -= 1
            counterA[25] -= 1
        elif counterA[25] >= 3:
            counterA[25] -= 3
        else:
            print("NO")
            exit()

print("YES")