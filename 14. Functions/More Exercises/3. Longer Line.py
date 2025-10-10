import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def dist_to_center(x, y):
    return math.sqrt(x ** 2 + y ** 2)

def format_point(x, y):
    return f"({math.floor(x)}, {math.floor(y)})"

def print_longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    line1_len = distance(x1, y1, x2, y2)
    line2_len = distance(x3, y3, x4, y4)

    if line1_len >= line2_len:
        # Find which point is closer to center for line 1
        if dist_to_center(x1, y1) <= dist_to_center(x2, y2):
            print(f"{format_point(x1, y1)}{format_point(x2, y2)}")
        else:
            print(f"{format_point(x2, y2)}{format_point(x1, y1)}")
    else:
        # Find which point is closer to center for line 2
        if dist_to_center(x3, y3) <= dist_to_center(x4, y4):
            print(f"{format_point(x3, y3)}{format_point(x4, y4)}")
        else:
            print(f"{format_point(x4, y4)}{format_point(x3, y3)}")

# Read input
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print_longer_line(x1, y1, x2, y2, x3, y3, x4, y4)