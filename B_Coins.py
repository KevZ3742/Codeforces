# http://codeforces.com/contest/47/problem/B
# rating: 1200

combinations = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]

inputs = []
for _ in range(3):
    result = str(input())
    
    if result[1] == "<":
        result = result[::-1]
        result = result.replace("<", ">")

    inputs.append(result)

toPrint = ""
for combination in combinations:
    ok = True
    for i in inputs:
        l, r = i.split(">")
        if combination.index(l) > combination.index(r):
            ok = False
            break
    
    if ok:
        toPrint = combination[::-1]
        break

if toPrint == "":
    toPrint = "Impossible"

print(toPrint)