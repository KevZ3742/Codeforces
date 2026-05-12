# C. Phase Shift
# https://codeforces.com/problemset/problem/1735/C
# rating: 1400

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    q = [-1] * 26
    free = list(range(26))
    chainHead = list(range(26))
    chainTail = list(range(26))
    assigned = 0
    toPrint = []

    for ch in s:
        c = ord(ch) - ord('a')
        if q[c] != -1:
            toPrint.append(chr(q[c] + ord('a')))
            continue

        forbidden = chainTail[c]
        remaining = 26 - assigned

        if remaining == 1:
            chosen = free[0]
        else:
            chosen = -1
            for v in free:
                if v != forbidden:
                    chosen = v
                    break
            if chosen == -1:
                chosen = free[0]

        q[c] = chosen
        free.remove(chosen)
        assigned += 1

        head = chainHead[chosen]
        tail = chainTail[c]
        chainTail[head] = tail
        chainHead[tail] = head

        toPrint.append(chr(chosen + ord('a')))

    print(''.join(toPrint))