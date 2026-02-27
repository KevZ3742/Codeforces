# C. Specialty String
# https://codeforces.com/contest/2200/problem/C
# rating: ?

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if stack:
        print("NO")
    else:
        print("YES")