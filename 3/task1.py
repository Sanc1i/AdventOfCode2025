def getNumber(line):
    arr = [int(char) for char in line[:-1]]
    number = max(arr[:-1]) * 10
    idx = arr.index(max(arr[:-1]))
    arr.pop(idx)
    number += max(arr[idx:])
    return number

result = 0
with open("puzzle.txt", 'r') as file:
    for line in file:
        number = getNumber(line)
        result += number
        print(result, number)
