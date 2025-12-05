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


def findElements(arr, element):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if (arr[mid][0] <= element):
            if (arr[mid][1] >= element):
                return True
            else:
                left = mid + 1
        else:
            right = mid - 1
    return False

with open("puzzle.txt", 'r') as file:
    lines = file.readlines()
    fileHalfIdx = lines.index('\n')
    ranges = [list(map(int, line.split('-'))) for line in lines[:fileHalfIdx]]
    products = list(map(int, lines[(fileHalfIdx + 1):]))

    total = 0
    merged = sortAndMerge(ranges)
    for product in products:
        if(findElements(merged, product)):
            total += 1

    print(total)
