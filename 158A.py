# A. Next Round
# https://codeforces.com/contest/158/problem/A
# rating: 800

contestants = str(input())
contestants = [int(i) for i in contestants.split()]

scores = str(input())
scores = [int(i) for i in scores.split()]

k = scores[contestants[1] - 1]
advancers = 0

for n in scores:
    if k == 0 and n > 0:
        advancers+=1
    elif k != 0 and n >= k:
        advancers+=1
    else:
        break

print(advancers)