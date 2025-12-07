beams = {}

with open("puzzle.txt", 'r') as file:
    lines = [line.rstrip() for line in file.readlines()]

    # FIX 1: Correct dictionary assignment
    if "S" in lines[0]:
        beams[lines[0].index("S")] = 1

        # FIX 2: Iterate row by row, starting from row 1
    for i in range(1, len(lines)):
        next_beams = {}

        # FIX 3: Iterate through position AND count (using .items())
        for beam_pos, count in beams.items():

            # Boundary check
            if beam_pos < 0 or beam_pos >= len(lines[i]):
                continue

            if lines[i][beam_pos] == "^":
                # SPLIT: Pass the existing 'count' to neighbors
                # Using .get() prevents errors if the key doesn't exist yet
                next_beams[beam_pos + 1] = next_beams.get(beam_pos + 1, 0) + count
                next_beams[beam_pos - 1] = next_beams.get(beam_pos - 1, 0) + count
            else:
                # STRAIGHT: Pass the existing 'count' down
                next_beams[beam_pos] = next_beams.get(beam_pos, 0) + count

        beams = next_beams

    # FIX 4: Sum the values, not the keys
    total = sum(beams.values())
    print(total)