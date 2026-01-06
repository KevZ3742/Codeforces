# https://codeforces.com/problemset/problem/25/A
# rating: 1300

count = int(input())
nums = list(map(int, input().split()))

even = 0
odd = 0
lastEven = 0
lastOdd = 0

for i in range(count):
    if nums[i] % 2 == 0:
        even+=1
        lastEven = i
    else:
        odd+=1
        lastOdd = i
    
    if odd >= 2 and even == 1:
        print(lastEven + 1)
        break
    elif even >= 2 and odd == 1:
        print(lastOdd + 1)
        break
