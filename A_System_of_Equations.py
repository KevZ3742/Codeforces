# rating: 800

n, m = map(int, input().split())

pairs = 0
for a in range(1001):
    b = n - a * a
    
    if a + b * b == m and b >= 0:
        pairs += 1

print(pairs)