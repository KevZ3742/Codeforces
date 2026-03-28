# C. Move Brackets
# https://codeforces.com/contest/1374/problem/C
# rating: 1000

t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input()
    
    stack = []
    
    prev = ""
    for char in s:
        if char == ")":
            if prev == "(":
                stack.pop()
                
                if stack:
                    prev = stack[-1]
                else:
                    prev = ""
            else:
                stack.append(char)
                prev = char
        else:
            stack.append(char)
            prev = char
            
    print(len(stack) // 2)