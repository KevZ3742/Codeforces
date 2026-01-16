# https://codeforces.com/contest/63/problem/A
# rating: 900

n = int(input())

value = {
    'rat':0,
    'child':1,
    'woman':1,
    'man':2,
    'captain':3
}

crew = []
for _ in range(n):
    name, status = map(str, input().split())
    member = [value[status], name]

    crew.append(member)

crew.sort(key=lambda x: x[0])

for member in crew:
    print(member[1])