# Author: Youssef AITBOUDDROUB

import random
import sys

# Increase the Python recursion limit to handle deep recursion without hitting the recursion depth limit
sys.setrecursionlimit(10**6)  # Example: increase the limit to 1,000,000

# Define the size of the maze
rows, columns = 50, 50

def generate_maze(rows, cols):
    """
    Generates a maze using the Depth-First Search (DFS) algorithm.

    Parameters:
    - rows (int): The number of rows in the maze.
    - cols (int): The number of columns in the maze.

    Returns:
    - maze (list of lists): The generated maze as a 2D list, where 1 represents walls and 0 represents paths.
    - start (tuple): The starting position in the maze.
    - goal (tuple): The goal position in the maze, placed as far as possible from the start.
    """
    # Initialize the maze with walls (1s)
    maze = [[1 for _ in range(cols)] for _ in range(rows)]

    # Randomly choose a starting position on the grid, ensuring it's on an odd row and column
    start = (random.randrange(0, rows, 2), random.randrange(0, cols, 2))
    maze[start[0]][start[1]] = 0  # Mark the start position as a path

    goal = None  # To be determined based on the furthest point reached by DFS
    max_distance = -1  # Keep track of the furthest distance reached from the start

    def DFS(x, y, distance=0):
        """
        Performs Depth-First Search recursively to generate the maze.

        Parameters:
        - x, y (int): Current position in the maze.
        - distance (int): Current distance from the start position.
        """
        nonlocal goal, max_distance
        # Possible directions to move: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)  # Randomize directions to ensure maze randomness

        for dx, dy in directions:
            nx, ny = x + dx*2, y + dy*2  # Calculate the next cell's position

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
                # Carve paths between the current cell and the next cell
                maze[x+dx][y+dy] = 0
                maze[nx][ny] = 0
                DFS(nx, ny, distance + 1)  # Recurse from the next cell

        # Update the goal position if the current position is the furthest from the start so far
        if distance > max_distance:
            max_distance = distance
            goal = (x, y)

    # Start DFS from the chosen starting position
    DFS(start[0], start[1])
    
    return maze, start, goal

def save_maze(maze, start, goal, filename):
    """
    Saves the generated maze to a text file.

    Parameters:
    - maze (list of lists): The maze to save.
    - start (tuple): The starting position in the maze.
    - goal (tuple): The goal position in the maze.
    - filename (str): The name of the file to save the maze to.
    """
    with open(filename, 'w') as file:
        file.write(f"{start[0]} {start[1]}\n")
        file.write(f"{goal[0]} {goal[1]}\n")
        for row in maze:
            file.write(' '.join(str(cell) for cell in row) + '\n')

# Generate and save the maze
maze, start, goal = generate_maze(rows, columns)
save_maze(maze, start, goal, 'maze_matrix.txt')
print(f"Generated a {rows}x{columns} maze and saved to 'maze_matrix.txt'")
