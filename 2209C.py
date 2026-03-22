# C. Find the Zero
# https://codeforces.com/contest/2209/problem/C
# rating: ?

import sys
input = sys.stdin.readline

def query(i, j):
    print(f"? {i} {j}", flush=True)
    response = int(input())

    if response == -1:
        sys.exit()
        
    return response

t = int(input())
for _ in range(t):
    n = int(input())
    
    counter = 1
    found = False

    for i in range(2, n + 2):
        response = query(counter, i)

        if response == 1:
            print(f"! {counter}", flush=True)
            found = True
            break
        else:
            counter = i

    if not found:
        print(f"! {counter}", flush=True)

# wa