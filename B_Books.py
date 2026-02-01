# https://codeforces.com/problemset/problem/279/B
# rating: 1400

data = list(map(int, input().split()))
books = list(map(int, input().split()))

l = 0
minutes = 0
maxBooks = 0

for r in range(data[0]):
    minutes += books[r]

    while minutes > data[1]:
        minutes -= books[l]
        l += 1

    maxBooks = max(maxBooks, r - l + 1)
    
print(maxBooks)