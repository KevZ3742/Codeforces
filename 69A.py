# A. Young Physicist
# https://codeforces.com/contest/69/problem/A
# rating: 1000

count = int(input())

sumVector = [0, 0, 0]

for i in range(count):
    vector = list(map(int, input().split()))

    sumVector[0] += vector[0]
    sumVector[1] += vector[1]
    sumVector[2] += vector[2]

if sumVector == [0, 0, 0]:
    print("YES")
else:
    print("NO")