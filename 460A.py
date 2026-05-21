# A. Vasya and Socks
# https://codeforces.com/problemset/problem/460/A
# rating: 900

n, m = map(int, input().split())

toPrint = 0
counter = 0
while n > 0:
    toPrint += 1
    n -= 1
    counter += 1
    if counter == m:
        n += 1
        counter = 0
        
print(toPrint)