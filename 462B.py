# B. Appleman and Card Game
# https://codeforces.com/problemset/problem/462/B
# rating: 1300

from collections import Counter

n, k = map(int, input().split())
letters = Counter(input())
counts = sorted(list(letters.values()), reverse=True)

coins = 0
for count in counts:
    if count >= k:
        coins += k * k
        break
    else:
        coins += count * count
        k -= count

print(coins)