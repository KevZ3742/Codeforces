# rating: 800

count = int(input())

problemCounter = 0

for i in range(count):
    solution = str(input())
    solutions = solution.split()

    sure = solutions.count("1")
    if sure >= 2:
        problemCounter+=1

print(problemCounter)