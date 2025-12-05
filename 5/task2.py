def sortAndMerge(arr):
    a = sorted(arr, key=lambda x: x[0])
    merged = [a[0]]
    for iteam in a[1:]:
        lastMerged = merged[-1]

        if iteam[0] <= lastMerged[1]:
            lastMerged[1] = max(iteam[1], lastMerged[1])
        else:
            merged.append(iteam)
    return merged


with open("puzzle.txt", 'r') as file:
    lines = file.readlines()
    fileHalfIdx = lines.index('\n')
    ranges = [list(map(int, line.split('-'))) for line in lines[:fileHalfIdx]]
    products = list(map(int, lines[(fileHalfIdx + 1):]))

    total = 0
    merge = sortAndMerge(ranges)
    for iteam in merge:
        total += iteam[1] - iteam[0] + 1
    print(total)
