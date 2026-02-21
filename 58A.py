# A. Chat room
# https://codeforces.com/contest/58/problem/A
# rating: 1000

letters = str(input())

hello = "hello"
i = 0

for char in letters:
    if char == hello[i]:
        i += 1
        if i == len(hello):
            break
        
if i == len(hello):
    print("YES")
else:
    print("NO")