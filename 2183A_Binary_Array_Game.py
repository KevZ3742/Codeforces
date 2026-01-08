# https://codeforces.com/contest/2183/problem/A
# rating: ?

testCases = int(input())

for i in range(testCases):
    n = int(input())
    a = list(map(int, input().split()))

    if a == [0]:
        print("Alice")
    elif 0 not in a:
        print("Alice")
    elif a[0] or a[-1] == 1:
        print("Alice")
    else:
        print("Bob")