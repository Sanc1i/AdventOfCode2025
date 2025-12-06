rows = []
operands = []

with open("puzzle.txt", 'r') as file:
    lines = file.readlines()
    for line in lines[:-1]:
        rows.append([int(num) for num in line.split()])
    operands = [0 if op == "+" else 1 for op in lines[-1].split()]
total = 0
for i in range(len(operands)):
    sum = operands[i]
    if sum == 0:
        for j in range(len(rows)):
            sum += rows[j][i]
        total += sum    
    else:
        for j in range(len(rows)):
            sum *= rows[j][i]
        total += sum
print(total)

