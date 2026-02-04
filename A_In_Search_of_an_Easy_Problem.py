# rating: 800

n = int(input())
a = list(map(int, input().split()))

for i in a:
    if i == 1:
        print("HARD")
        exit()

print("EASY")