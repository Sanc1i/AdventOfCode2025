from collections import deque

indicators = []
buttons = []

def getNextStages(code, buttons):
    codes = []
    for button in buttons:
        temp = list(code)
        for num in button:
            temp[num] = 0 if temp[num] else 1
        codes.append(tuple(temp))
    return codes

def findShortest(indicator, buttons):
    startStage = tuple([0 for _ in range(len(indicator))])
    queue = deque([(startStage, 0)])
    visited = {startStage}
    
    while queue:
        currentStage, turns = queue.popleft()
        if currentStage == tuple(indicator):
            print(turns)
            return turns
        
        for nextStage in getNextStages(currentStage, buttons):
            if nextStage not in visited:
                visited.add(nextStage)
                queue.append((nextStage, turns + 1))
    
    return -1

with open("puzzle.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        input_data = line.split(" ")
        indicators.append([0 if char == '.' else 1 for char in input_data[0][1:-1]])
        buttons.append([[int(num) for num in arr[1:-1].split(',')] for arr in input_data[1:-1]])

total = 0
for i in range(len(indicators)):
    total += findShortest(indicators[i], buttons[i])

print(total)
