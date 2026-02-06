# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    subMax = [0] * n
    subMax[-1] = p[-1]
    for i in range(n - 2, -1, -1):
        subMax[i] = max(p[i], subMax[i + 1])

    for i in range(n):
        if p[i] != subMax[i]:
            j = n - 1
            while p[j] != subMax[i]:
                j -= 1

            p[i:j + 1] = reversed(p[i:j + 1])
            break

    print(*p)