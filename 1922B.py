# B. Forming Triangles
# https://codeforces.com/problemset/problem/1922/B
# rating: 1200

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    freq = [0] * (n + 1)
    for x in a:
        freq[x] += 1
    
    toPrint = 0
    total = 0 
    
    for x in range(n + 1):
        count = freq[x]

        if count >= 3:
            toPrint += count * (count - 1) * (count - 2) // 6

        if count >= 2:
            toPrint += (count * (count - 1) // 2) * total
        
        total += count
    
    print(toPrint)