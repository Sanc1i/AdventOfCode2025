import sys

sys.setrecursionlimit(5000) 

total = 0
lines = []
maxLev = 0

def tree_rec(lev, index):
    global total
    
    if lev == maxLev:
        total += 1
        return

    if lines[lev][index] == "^":
        tree_rec(lev + 1, index - 1)
        tree_rec(lev + 1, index + 1)
    else:
        tree_rec(lev + 1, index)

with open("puzzle.txt", 'r') as file:
    lines = [line.rstrip() for line in file.readlines()]
    
    maxLev = len(lines)
    
    if "S" in lines[0]:
        start_index = lines[0].index("S")
        tree_rec(1, start_index)
    
    print(f"Total paths reaching bottom: {total}")
