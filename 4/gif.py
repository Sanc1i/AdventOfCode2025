import numpy as np
import imageio.v2 as imageio
import os

DISTANCE = 1

# --- Original Logic Functions ---

def checkNeighboor(dataset, x, y):
    total = -1
    # Note: dataset is a list of lists here
    rows = len(dataset)
    cols = len(dataset[0])
    
    for i in range(-DISTANCE, DISTANCE + 1):
        for j in range(-DISTANCE, DISTANCE + 1):
            # Safe boundary check
            if (0 <= (x + i) < cols) and (0 <= (y + j) < rows): 
                total += dataset[y + j][x + i]
    return total

def validateData(dataset):
    n = []
    for y in range(len(dataset)):
        for x in range(len(dataset[0])):
            if dataset[y][x] == 0:
                continue
            elif checkNeighboor(dataset, x, y) < 4:
                n.append([y, x])
    return n

def removeData(dataset, arr):
    for data in arr:
        dataset[data[0]][data[1]] = 0
    return dataset

# --- Visualization Helper ---

def create_frame(dataset, scale=10):
    """
    Converts the 0/1 list-of-lists into a visual image.
    scale=10 makes each 'pixel' 10x10 real pixels so the GIF is visible.
    """
    # Convert list of lists to numpy array
    arr = np.array(dataset, dtype=np.uint8)
    
    # Map 0 to Black (0), 1 to White (255) (or Green/Red, etc.)
    # Let's make 1s White (255) and 0s Black (0)
    img_data = arr * 255
    
    # Repeat elements to scale up the image (zoom in)
    # This makes a 50x50 grid look like a 500x500 image
    img_data = np.kron(img_data, np.ones((scale, scale)))
    
    return img_data.astype(np.uint8)

# --- Main Execution ---

# 1. Load Data (or create dummy data if file missing)
filename = "puzzle.txt"

if os.path.exists(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    dataset = [[1 if char == '@' else 0 for char in line] for line in lines]
    print(f"Loaded {filename}")
else:
    print(f"'{filename}' not found. Generating random noise for demonstration...")
    # Create a 50x50 random grid of 0s and 1s
    dataset = np.random.randint(0, 2, (50, 50)).tolist()

frames = []
total_removed = 0
iteration = 0

print("Processing...")

# 2. Add initial state to frames
frames.append(create_frame(dataset))

# 3. Main Loop
while True:
    # Check for items to remove
    to_remove = validateData(dataset)
    
    # If nothing to remove, stop
    if len(to_remove) == 0:
        break
        
    # Remove data
    removeData(dataset, to_remove)
    total_removed += len(to_remove)
    
    # Capture the state for the GIF
    frames.append(create_frame(dataset))
    
    iteration += 1
    if iteration % 5 == 0:
        print(f"Iteration {iteration}: removed {len(to_remove)} pixels")

print(f"Total Removed: {total_removed}")

# 4. Save GIF
output_file = "simulation.gif"
print(f"Saving GIF to {output_file}...")

# duration is time per frame in seconds (e.g., 0.1 = 10fps)
imageio.mimsave(output_file, frames, duration=0.2, loop=0) 

print("Done!")
