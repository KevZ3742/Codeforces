# B. Koxia and Permutation
# https://codeforces.com/problemset/problem/1770/B
# rating: 1000

t = int(input())

for i in range(t):
    n, k = map(int, input().split())

    nums = list(range(1, n + 1))

    toPrint = []
    l = 0
    r = n - 1
    while l <= r:
        toPrint.append(nums[r])
        r -= 1

        if l <= r:
            toPrint.append(nums[l])
            l += 1

    print(*toPrint)