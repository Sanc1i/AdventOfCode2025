DISTANCE = 1

def checkNeighboor(dataset, x, y):
    total = -1
    for i in range(-DISTANCE, DISTANCE + 1):
        for j in range(-DISTANCE, DISTANCE + 1):
            if (0 <= (x + i) < len(dataset)) and (0 <= (y + j) < len(dataset)): 
                total += dataset[y + j][x + i]
    return total


def validateData(dataset):
    n = []
    for y in range(len(dataset)):
        for x in range(len(dataset[0])):
            if dataset[y][x] == 0:
                continue
            elif checkNeighboor(dataset, x, y) < 4:
                n.append([y,x])
    return n

def removeData(dataset, arr):
    for data in arr:
        dataset[data[0]][data[1]] = 0
    return dataset

# dataset = np.loadtxt("test.txt", dtype=np.str)
# print(dataset)
with open("puzzle.txt", 'r') as file:
    lines = file.read().splitlines()

dataset = [[1 if char == '@' else 0 for char in line] for line in lines]
total = 0
while len(array := validateData(dataset)) > 0:
    removeData(dataset, array)
    total += len(array)

print(total)
