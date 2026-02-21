# A. Panoramix's Prediction
# https://codeforces.com/contest/80/problem/A
# rating: 800

n, m = map(int, input().split())

def isPrime(num):
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            return False
    return True

nextNum = n + 1
while not isPrime(nextNum):
    nextNum += 1

if nextNum == m:
    print("YES")
else:
    print("NO")