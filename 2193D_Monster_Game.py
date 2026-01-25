# https://codeforces.com/contest/2193/problem/D
# rating: ?

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    
    swordsNeeded = [0] * (n + 1)
    swordsNeeded[0] = 0
    for i in range(1, n + 1):
        swordsNeeded[i] = swordsNeeded[i - 1] + b[i - 1]

    score = 0

    difficulties = sorted(set(a))
    for difficulty in difficulties:
        swordsAvailable = sum(sword >= difficulty for sword in a)

        levels = 0
        for i in range(n + 1):
            
            if swordsNeeded[i] <= swordsAvailable:
                levels = i
            else:
                break

        score = max(difficulty * levels, score)

    print(score)

# tle