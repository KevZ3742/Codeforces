# A. Jzzhu and Children
# https://codeforces.com/contest/450/problem/A
# rating: 1000

n, m = map(int, input().split())
a = list(map(int, input().split()))

queue = list(range(n))
while len(queue) > 1:
    a[queue[0]] -= m
    if a[queue[0]] <= 0:
        queue.pop(0)
    else:
        toAppend = queue.pop(0)
        queue.append(toAppend)

print(queue[0] + 1)