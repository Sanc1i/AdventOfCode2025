import sys

# 1. Ray Casting: Standard algorithm to check if a point is inside a polygon
def is_point_in_polygon(x, y, poly_points):
    n = len(poly_points) - 1
    inside = False
    p1x, p1y = poly_points[0]
    for i in range(n + 1):
        p2x, p2y = poly_points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def do_segments_intersect(p1, p2, p3, p4):
    # Only check perpendicular segments (one horizontal, one vertical)
    seg1_horizontal = p1[1] == p2[1]
    seg2_vertical = p3[0] == p4[0]
    
    # We only care about crossing, so we swap if needed to ensure 
    # Seg1 is Horiz, Seg2 is Vert
    if seg1_horizontal and seg2_vertical:
        h_seg, v_seg = (p1, p2), (p3, p4)
    elif (p1[0] == p2[0]) and (p3[1] == p4[1]): # Seg1 Vert, Seg2 Horiz
        v_seg, h_seg = (p1, p2), (p3, p4)
    else:
        return False # Parallel segments don't cross in this simple check

    h_y = h_seg[0][1]
    h_x_min, h_x_max = min(h_seg[0][0], h_seg[1][0]), max(h_seg[0][0], h_seg[1][0])
    
    v_x = v_seg[0][0]
    v_y_min, v_y_max = min(v_seg[0][1], v_seg[1][1]), max(v_seg[0][1], v_seg[1][1])
    
    # FIX: Use STRICT inequalities (< instead of <=)
    # We allow touching at corners, we only ban crossing through the middle
    return (h_x_min < v_x < h_x_max) and (v_y_min < h_y < v_y_max)

def is_valid_rectangle(p1, p2, poly_points):
    x1, y1 = p1
    x2, y2 = p2
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    # 1. CENTER CHECK: Is the rectangle physically inside the polygon?
    # Without this, you might create a rectangle completely outside.
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    if not is_point_in_polygon(center_x, center_y, poly_points):
        return False

    # 2. EDGE COLLISION CHECK
    rect_edges = [
        ((min_x, min_y), (max_x, min_y)),
        ((max_x, min_y), (max_x, max_y)),
        ((max_x, max_y), (min_x, max_y)),
        ((min_x, max_y), (min_x, min_y)) 
    ]
    
    for i in range(4):
        r_start, r_end = rect_edges[i]
        for j in range(len(poly_points) - 1):
            if do_segments_intersect(r_start, r_end, poly_points[j], poly_points[j+1]):
                return False

    # 3. POLYGON POINT CHECK: Does the polygon dip INSIDE the rectangle?
    # This catches cases where the rectangle spans across a "bay" or empty space.
    for px, py in poly_points:
        # If a polygon vertex is strictly inside the rectangle, it's invalid
        if min_x < px < max_x and min_y < py < max_y:
            return False

    return True

# --- Main Execution ---
with open("test.txt", 'r') as file:
    points = [tuple(int(n) for n in line.split(',')) for line in file.readlines()]
    points.append(points[0]) 

max_area = 0

for i in range(len(points) - 1):
    for j in range(i + 1, len(points) - 1):
        
        # Optimization: Calculate area first. If it's small, don't waste time checking validity.
        w = abs(points[i][0] - points[j][0]) + 1
        h = abs(points[i][1] - points[j][1]) + 1
        area = w * h
        
        if area <= max_area:
            continue

        if is_valid_rectangle(points[i], points[j], points):
            max_area = area
            print(f"New Max: {max_area} (Points: {i}, {j})")

print(f"Final Max: {max_area}")
