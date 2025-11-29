def find_kate(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'k':
                return row, col
    return None


def is_valid_move(maze, row, col):
    return (0 <= row < len(maze) and
            0 <= col < len(maze[0]) and
            maze[row][col] != '#')


def find_exit(maze, row, col, visited):
    # If we're on the border, we're already out -> 0 moves needed
    if row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[0]) - 1:
        if maze[row][col] != '#':
            return 0

    visited[row][col] = True
    max_path = -1  # -1 means no path to exit found from here

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if (is_valid_move(maze, new_row, new_col) and
                not visited[new_row][new_col]):
            path = find_exit(maze, new_row, new_col, visited)
            if path >= 0:
                max_path = max(max_path, path + 1)

    visited[row][col] = False
    return max_path


rows = int(input())
maze = [list(input()) for _ in range(rows)]

kate_pos = find_kate(maze)
if kate_pos:
    visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    moves = find_exit(maze, kate_pos[0], kate_pos[1], visited)
    if moves >= 0:
        print(f"Kate got out in {moves} moves")
    else:
        print("Kate cannot get out")
