# rating: 900

k = int(input())
a = list(map(int, input().split()))

if k > sum(a):
    print(-1)
    exit()

a.sort(reverse=True)

months = 0
for height in a:
    if k <= 0:
        break

    k -= height
    months += 1
    
print(months)