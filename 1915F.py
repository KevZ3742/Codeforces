# F. Greetings
# https://codeforces.com/problemset/problem/1915/F
# rating: 1500

inv = 0

def merge(arr, l, m, r):
    global inv

    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[l + i]

    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]

            inv += (n1 - i)

            j += 1

        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        merge(arr, l, m, r)

t = int(input())

for _ in range(t):
    n = int(input())

    ranges = []

    for i in range(n):
        a, b = map(int, input().split())
        ranges.append((a, b))

    ranges.sort()
    bValues = [b for a, b in ranges]
    inv = 0

    mergeSort(bValues, 0, n - 1)

    print(inv)