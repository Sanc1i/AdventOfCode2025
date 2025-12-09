points = []

def calrect(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((abs(x2-x1) + 1) * (abs(y2 - y1) + 1))

with open("puzzle.txt", 'r') as file:
    points = [tuple(int(n) for n in line.split(',')) for line in file.readlines()]
max = 0
for i in range(len(points)):
    for j in range(len(points)):
        if i == j: 
            continue
        area = calrect(points[i], points[j])
        if (area > max):
            max = area 
print(max)
