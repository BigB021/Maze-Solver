# Author: Youssef AITBOUDDROUB

import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np
from matplotlib.colors import ListedColormap, Normalize
from queue import PriorityQueue
from matplotlib.animation import FuncAnimation

def ucs(maze, start, goal):
    """
    Performs the Uniform Cost Search (UCS) algorithm to find the shortest path in a maze.

    Parameters:
    - maze (numpy.ndarray): 2D array representing the maze.
    - start (tuple): Starting position (x, y) in the maze.
    - goal (tuple): Goal position (x, y) in the maze.

    Yields:
    - tuple of (path, current): Path is a list of tuples representing the positions from start to current.
                                Current is the current position (x, y) being processed.
    """
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    rows, columns = maze.shape
    frontier = PriorityQueue()
    frontier.put((0, start, [start]))
    visited = set()

    while not frontier.empty():
        cost, current, path = frontier.get()

        if current == goal:
            yield path, current  # Yield the final path to the goal
            return
        if current in visited:
            continue
        visited.add(current)

        yield path, current  # Yield current path for animation

        for d in directions:
            next_cell = (current[0] + d[0], current[1] + d[1])
            if 0 <= next_cell[0] < rows and 0 <= next_cell[1] < columns and maze[next_cell[0]][next_cell[1]] == 0:
                if next_cell not in visited:
                    frontier.put((cost + 1, next_cell, path + [next_cell]))


def load_maze(filename):
    """
    Load maze from a text file.

    Parameters:
    - filename (str): The name of the file containing maze information.

    Returns:
    - numpy.ndarray: The maze represented as a 2D array.
    - tuple: The starting position (row, column) in the maze.
    - tuple: The goal position (row, column) in the maze.
    """
    with open(filename, 'r') as file:
        start = tuple(map(int, file.readline().split()))  # Read start position
        goal = tuple(map(int, file.readline().split()))  # Read goal position
        maze = [[int(num) for num in line.split()] for line in file]
    return np.array(maze), start, goal

def visualize_maze(maze, path=None, start=None, goal=None, current=None):
    """_summary_
    Functionalities:
        Maze and Path Visualization, 
        Position Marking,
        Custom Color Map.

    Parameters:
        maze (numpy.ndarray): A 2D array representing the maze where 0 indicates a free path and 1 indicates a wall or an obstacle.
        path (list of tuple, optional): A list of tuples representing the coordinates of the path from the start to the current position. Each tuple is in the format (row, column). Default is None, which means no path has been found or is being visualized yet.
        start (tuple, optional): A tuple indicating the starting position in the maze with the format (row, column). Default is None.
        goal (tuple, optional): A tuple indicating the goal or destination position in the maze with the format (row, column). Default is None.
        current (tuple, optional): A tuple indicating the current position being explored in the maze with the format (row, column). This is useful for visualizing the progression of the search algorithm. Default is None.

    """
    # Make a copy of the maze for visualization
    maze_copy = np.copy(maze)
    if path is not None:
        for position in path:
            maze_copy[position[0], position[1]] = 2  # Mark the path with a distinct value
    
    # Mark the current exploration node
    if current is not None and maze[current[0], current[1]] != 3 and maze[current[0], current[1]] != 4:
        # Ensure the current position is neither the start nor the goal before marking
        maze_copy[current[0], current[1]] = 5  # Use a different value to mark the current position
    
    # Mark start and goal positions
    if start is not None:
        maze_copy[start[0], start[1]] = 3  # Mark start with a distinct value
    if goal is not None:
        maze_copy[goal[0], goal[1]] = 4  # Mark goal with a distinct value

    # Define a custom colormap: 0 for free space, 1 for walls, 2 for the path, 3 for start, 4 for goal, 5 for current exploration node
    cmap = ListedColormap(['white', 'black', 'red', 'blue', 'green', 'yellow'])  # Free space, walls, path, start, goal, current
    norm = Normalize(vmin=0, vmax=5)

    # Display the maze
    ax.clear()  # Clear previous contents
    ax.imshow(maze_copy, cmap=cmap, norm=norm)
    plt.xticks([]), plt.yticks([])  # Hide the axes ticks
    plt.title('Maze Visualization')
    plt.draw()  # Redraw the current figure

def update(frame):
    """
    Update function for animation. Draws the current state of the maze.

    Parameters:
    - frame: The current frame data, consisting of the path and current position.
    """
    path, current = frame
    visualize_maze(maze, path=path, current=current, start=start, goal=goal)

if __name__ == "__main__":
    maze, start, goal = load_maze("maze_matrix.txt")
    fig, ax = plt.subplots(figsize=(10, 10))

    # Generate all states from UCS for animation
    states = list(ucs(maze, start, goal))

    # Initialize animation
    anim = FuncAnimation(fig, update, frames=states, interval=20, repeat=False)  # Adjust interval for speed

    plt.show()
