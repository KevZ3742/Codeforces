# A. Bear and Big Brother
# https://codeforces.com/contest/791/problem/A
# rating: 800

limak, bob = map(int, input().split())

years = 0
while limak <= bob:
    years += 1
    limak = limak * 3
    bob = bob * 2

print(years)