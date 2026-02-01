# https://codeforces.com/contest/463/problem/B
# rating: 1100

n = int(input())
h = [0] + list(map(int, input().split()))

money = 0
energy = 0
for i in range(n + 1):
    if i + 1 >= n + 1:
        break
        
    energy -= h[i + 1] - h[i]

    if energy < 0:
        money += abs(energy)
        energy = 0

print(money)