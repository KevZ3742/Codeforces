# rating: 800

n, t = map(int, input().split())
s = str(input())

for _ in range(t):
    s = s.replace("BG", "GB")

print(s)