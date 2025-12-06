import math
lines = []

with open("puzzle.txt", 'r') as file:
    for line in file.readlines():
        lines.append(line[::-1][1:])

total, i  = 0, 0
numbers = []
while(i < len(lines[0])):
    num = 0
    for j in range(len(lines)):
        if lines[j][i] == " ":
            continue
        elif lines[j][i] == '*':
            numbers.append(num)
            total += math.prod(numbers)
            numbers.clear()
            num = 0
            i += 1
        elif lines[j][i] == "+":
            numbers.append(num)
            total += sum(numbers)
            numbers.clear()
            num = 0
            i +=1
        else:
            num *= 10
            num += int(lines[j][i])
    if num != 0:
        numbers.append(num)
    i += 1
print(total)

