def getNumber(line):
    arr = [int(char) for char in line[:-1]]
    while(len(arr) > 12):
        isRemoved = False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i+1]:
                arr.pop(i)
                isRemoved = True
                break
        if not isRemoved:
            arr.pop()
    return int("".join(map(str,arr)))

result = 0
with open("puzzle.txt", 'r') as file:
    for line in file:
        number = getNumber(line)
        result += number
    print(result)
