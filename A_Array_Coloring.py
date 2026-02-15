# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    flag = True
    prev = -1
    for i in a:
        if i % 2 == prev:
            flag = False
            break
        
        prev = i % 2

    if flag:
        print("YES")
    else:
        print("NO")