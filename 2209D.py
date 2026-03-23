# D. Ghostfires
# https://codeforces.com/contest/2209/problem/D
# rating: ?

t = int(input())
 
for _ in range(t):
    r, g, b = map(int, input().split())

    toPrint = []

    counter = {"R": r, "G": g, "B": b}
    prev = ["", "", ""]
    states = {"R": True, "G": True, "B": True}

    if counter["R"] == 0:
        states["R"] = False

    if counter["G"] == 0:
        states["G"] = False

    if counter["B"] == 0:
        states["B"] = False
    
    while states["R"] or states["G"] or states["B"]:
        canUse = [key for key, value in states.items() if value is True]
        toUse = max(canUse, key=lambda k: (counter[k], k == prev[1]))

        toPrint.append(toUse)
        counter[toUse] -= 1

        states = {"R": True, "G": True, "B": True}

        prev[2] = prev[1]
        prev[1] = prev[0]
        prev[0] = toUse

        states[prev[0]] = False
        states[prev[1]] = True
        states[prev[2]] = False

        if counter["R"] == 0:
            states["R"] = False

        if counter["G"] == 0:
            states["G"] = False

        if counter["B"] == 0:
            states["B"] = False

    print("".join(toPrint))