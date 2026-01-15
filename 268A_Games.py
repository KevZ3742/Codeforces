# https://codeforces.com/contest/268/problem/A
# rating: 800

n = int(input())

teams = 0
for _ in range(n):
    teams.append(list(map(int, input().split())))

counter = 0
for i in range(n):
    for j in range(n):
        if i != j:
            if teams[i][0] == teams[j][1]:
                count += 1

print(count)