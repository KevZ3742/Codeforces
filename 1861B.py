# B. Two Binary Strings
# https://codeforces.com/problemset/problem/1861/B
# rating: 1000

t = int(input()) 

for _ in range(t):
    a = input()
    b = input()
    
    ok = False
    for i in range(len(a) - 1):
        if a[i] == b[i] == '0' and a[i + 1] == b[i + 1] == '1':
            ok = True
            break
    
    print("YES" if ok else "NO")