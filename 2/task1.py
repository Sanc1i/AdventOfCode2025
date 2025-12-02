import re

def ParseLine(line):
    return re.split(r'[,-]', line)


with open("puzzle.txt", "r") as file:
    line = file.readline()
    num_array = ParseLine(line)
    output = 0
    for i in range(0, len(num_array) - 1, 2):
        for num in range(int(num_array[i]), int(num_array[i+1]) + 1):
            length = len(str(num))
            if (length % 2 != 0):
                continue
            power = pow(10,length/2)
            if ((num % power) == (num // power)):
                output += num
    print(output)
