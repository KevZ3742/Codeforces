# rating: ?

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    
    level = 0
    swordsNeeded = 0
    score = 0

    for i in range(1, n + 1):
        while level < n and swordsNeeded + b[level] <= i:
            swordsNeeded += b[level]
            level += 1

        score = max(score, a[i - 1] * level)

    print(score)