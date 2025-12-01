rotation = 50
output = 0
filename = "puzzle.txt"

def new_rotation(line):
    number = int(line[1::])
    global rotation, output
    if "R" in line:
        rotation += number
        while rotation > 99:
            rotation -= 100 
            output += 1
    else:
        if rotation == 0:
            output -= 1
        rotation -= number
        while rotation < 0:
            rotation += 100
            output += 1
        if rotation == 0:
            output += 1

with open(filename, "r") as f:
    for line in f:
        print(rotation, output)
        new_rotation(line)
    print(output)
