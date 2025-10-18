def read_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append(input().split())
    return matrix


def is_valid(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


def find_connected_dots(matrix, row, col, visited):
    if not is_valid(row, col, matrix) or matrix[row][col] != '.' or (row, col) in visited:
        return 0

    visited.add((row, col))
    count = 1

    # Check all 4 directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        count += find_connected_dots(matrix, row + dx, col + dy, visited)

    return count


def solve(matrix):
    max_dots = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == '.':
                visited = set()
                max_dots = max(max_dots, find_connected_dots(matrix, row, col, visited))

    return max_dots


n = int(input())
matrix = read_matrix(n)
result = solve(matrix)
print(result)
