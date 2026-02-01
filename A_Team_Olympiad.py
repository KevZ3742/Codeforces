# rating: 800

n = int(input())
t = list(map(int, input().split()))

programming = []
math = []
pe = []

for i in range(n):
    if t[i] == 1:
        programming.append(i + 1)
    elif t[i] == 2:
        math.append(i + 1)
    else:
        pe.append(i + 1)

teamCounter = 0
teams = []
while len(programming) >= 1 and len(math) >= 1 and len(pe) >= 1:
    toAppend = [programming.pop(), math.pop(), pe.pop()]
    teams.append(toAppend)
    teamCounter += 1

print(teamCounter)
for team in teams:
    print(*team)