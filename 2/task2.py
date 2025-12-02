import re

def parseLine(line):
    return re.split(r'[,-]', line)

def hasReapetingPattern(num):
    length = len(str(num))
    for size in range (1, length // 2 + 1):
        if (length % size == 0):
            pattern = str(num)[:size]
            if (pattern * (length // size) == str(num)):
                return True
    return False
    


with open("puzzle.txt", "r") as file:
    line = file.readline()
    num_array = parseLine(line)
    output = 0
    for i in range(0, len(num_array) - 1, 2):
        for num in range(int(num_array[i]), int(num_array[i+1]) + 1):
            if(hasReapetingPattern(num)):
                output += num
    print(output)
