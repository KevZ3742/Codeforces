# https://codeforces.com/contest/770/problem/A
# rating: 800

n, k = map(int, input().split())

counter = 0
password = ""
for _ in range(n):
    if counter == k:
        counter = 0

    password += chr(97 + counter)
    counter += 1

print(password)