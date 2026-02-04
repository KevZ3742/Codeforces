# rating: 1100

n, m = map(int, input().split())
a = list(map(int, input().split()))

maxZlotys = 0
minZlotys = 0

arr = a.copy()
for i in range(n):
    maxAIndex = arr.index(max(arr))
    maxZlotys += arr[maxAIndex]
    arr[maxAIndex] -= 1

arr = a.copy()
for i in range(n):
    if len(arr) == 0:
        break
    
    minAIndex = arr.index(min(arr))
    minZlotys += arr[minAIndex]
    arr[minAIndex] -= 1
    
    if arr[minAIndex] <= 0:
        arr.pop(minAIndex)

print(maxZlotys, minZlotys)