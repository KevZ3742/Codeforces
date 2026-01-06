# https://codeforces.com/problemset/problem/492/B
# rating: 1200

data = list(map(int, input().split()))
lanterns = list(map(int, input().split()))
lanterns.sort()

largestGap = 0

for i in range(data[0]):
    if i == 0:
        prev = 0
    else:
        prev = lanterns[i-1]

    largestGap = max(largestGap, lanterns[i]-prev)

print(max(largestGap / 2, lanterns[0], data[1] - lanterns[-1]))