import random

def generate_maze(rows, cols):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            maze[r][c] = random.choice([0, 1])
    maze[1][1] = 0
    maze[rows - 2][cols - 2] = 0
    return maze
