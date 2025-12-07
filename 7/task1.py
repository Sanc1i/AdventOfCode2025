beams = []

with open("puzzle.txt", 'r') as file:
    lines = [line.rstrip() for line in file.readlines()]
    if "S" in lines[0]:
        beams.append(lines[0].index("S"))

    total = 0

    for i in range(2, len(lines), 2):
        next_beams = []

        for beam in beams:
            if beam < 0 or beam >= len(lines[i]):
                continue

            if lines[i][beam] == "^":
                if (beam + 1) not in next_beams:
                    next_beams.append(beam + 1)
                if (beam - 1) not in next_beams:
                    next_beams.append(beam - 1)
                total += 1
            else:
                if beam not in next_beams:
                    next_beams.append(beam)
        beams = next_beams

    print(total)
