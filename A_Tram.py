# rating: 800

n = int(input())

inTram = 0
maxCap = 0
for _ in range(n):
    a, b = map(int, input().split())
    inTram += b - a
    inTram = max(inTram, 0)
    maxCap = max(maxCap, inTram)

print(maxCap)