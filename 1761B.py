# B. Elimination of a Ring
# https://codeforces.com/problemset/problem/1761/B
# rating: 1000

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    toPrint = 0

    toPop = -1
    while a:
        if len(a) == 1:
            print("here",1)
            toPrint += 1
            a.pop()
        elif len(a) == 2 and a[0] != a[1]:
            print("here",2)
            toPrint += 2
            a.pop()
            a.pop()
        elif toPop == -len(a):
            print("here",3)
            toPrint += 1
            a.pop()
            a.pop()
            toPop = -1
        elif a[toPop - 1] == a[toPop + 1]:
            print("here",4,toPop)
            toPop -= 1
        else:
            print("here",5,toPop)
            toPrint += 1
            a.pop(toPop)
            toPop = -1

        print(a, toPrint)
    
    print(toPrint)

    # wa