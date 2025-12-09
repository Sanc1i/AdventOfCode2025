import math
chains = []
distance = {}

def straightLineDistance(point1, point2):
    return math.dist(point1, point2)

def addchain(idx1, idx2, chain_idx1, chain_idx2):
    if chain_idx1 == -1 and chain_idx2 == -1:
        chains.append([idx1, idx2])
    elif chain_idx1 != -1 and chain_idx2 == -1:
        chains[chain_idx1].append(idx2)
    elif chain_idx1 == -1 and chain_idx2 != -1:
        chains[chain_idx2].append(idx1)
    elif chain_idx1 == chain_idx2:
        pass
    else:
        target, source = (chain_idx1, chain_idx2) if chain_idx1 < chain_idx2 else (chain_idx2, chain_idx1)
        chains[target].extend(chains[source])
        chains.pop(source)


with open("puzzle.txt", 'r') as file:
    points = [tuple(int(n) for n in line.split(',')) for line in file.readlines()]
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            key = f"{i} {j}"
            distance[key] = straightLineDistance(points[i], points[j])
    
    sortedDistances = sorted(distance.items(), key=lambda item: item[1])

    j = 0
    p1, p2 = 0, 0 
    
    while len(chains) != 1 or len(chains[0]) < len(points):
        if j >= len(sortedDistances):
             break
             
        key, value = sortedDistances[j]
        p1_str, p2_str = key.split()
        p1, p2 = int(p1_str), int(p2_str)
        
        chain1, chain2 = -1, -1
        for i in range(len(chains)):
            if p1 in chains[i]:
                chain1 = i
            if p2 in chains[i]:
                chain2 = i
        
        addchain(p1, p2, chain1, chain2)
        j += 1

    print(points[p1][0] * points[p2][0])
