from collections import deque

indicators = []
buttons = []

def checkDeadSet(indicator, stage):
    for i in range(len(indicator)):
        if stage[i] > indicator[i]:
            return True
    return False

def getNextStages(code, buttons):
    codes = []
    for button in buttons:
        temp = list(code)
        for num in button:
            temp[num] += 1 
        codes.append(tuple(temp))
    return codes

def findShortest(indicator, buttons):
    startStage = tuple([0 for _ in range(len(indicator))])
    queue = deque([(startStage, 0)])
    visited = {startStage}
    
    deadset = set()
    
    while queue:
        currentStage, turns = queue.popleft()
        if currentStage == tuple(indicator):
            return turns
        
        for nextStage in getNextStages(currentStage, buttons):
            print(nextStage)
            if nextStage in deadset:
                continue
            if checkDeadSet(indicator, nextStage):
                deadset.add(nextStage)
                continue
            if nextStage not in visited:
                visited.add(nextStage)
                queue.append((nextStage, turns + 1))
    
    return -1

with open("puzzle.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        input_data = line.split(" ")
        indicators.append([int(num) for num in input_data[-1][1:-2].split(',')])
        buttons.append([[int(num) for num in arr[1:-1].split(',')] for arr in input_data[1:-1]])
total = 0
for i in range(len(indicators)):
    print(i)
    total += findShortest(indicators[i], buttons[i])

print(total)
