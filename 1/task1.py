rotation = 50
output = 0
filename = "puzzle.txt"

def new_rotation(line):
    number = int(line[1::])
    global rotation
    if "R" in line:
        rotation += number
        while rotation > 99:
            rotation -= 100 
    else:
        rotation -= number
        while rotation < 0:
            rotation += 100

with open(filename, "r") as f:
    for line in f:
        new_rotation(line)
        if rotation == 0:
            output += 1
    print(output)
