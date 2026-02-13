# rating: 1300

a, b, c = map(int, input().split())

mod = 1073741824 

n = a * b * c
divisors = [0] * (n + 1) 
for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        divisors[j] += 1

total = 0
for i in range(1, a + 1):
    for j in range(1, b + 1):
        ij = i * j
        for k in range(1, c + 1):
            total += divisors[ij * k]

print(total % mod)