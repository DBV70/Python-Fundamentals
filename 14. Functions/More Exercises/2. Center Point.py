import math

def center_point(x1, y1, x2, y2):
    # Calculate distances from (0, 0)
    dist1 = math.sqrt(x1 ** 2 + y1 ** 2)
    dist2 = math.sqrt(x2 ** 2 + y2 ** 2)
    # Format to lower integer
    x1_int, y1_int = math.floor(x1), math.floor(y1)
    x2_int, y2_int = math.floor(x2), math.floor(y2)
    if dist1 <= dist2:
        print(f"({x1_int}, {y1_int})")
    else:
        print(f"({x2_int}, {y2_int})")

# Read input
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

center_point(x1, y1, x2, y2)