# https://codeforces.com/problemset/problem/1352/C
# rating: 1200

def getNumMultiples(n, max):
    return max // n + 1

testCases = int(input())

for _ in range(testCases):
    n, k = map(int, input().split())

    setSize = n-1
    blocks = (k - 1) // setSize

    print(k + blocks)