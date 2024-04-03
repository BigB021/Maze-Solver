# Maze Solver Project

This Maze Solver Project is an intriguing Python application that generates a maze using a Depth-First Search (DFS) algorithm and then implements both DFS and Uniform Cost Search (UCS) algorithms to find a path from the start point to the goal. The project is designed to demonstrate algorithmic thinking, recursion, and pathfinding strategies in a visually engaging manner. Below you will find detailed information on how to set up, run, and understand the project.

## Features

Maze Generation: Create a randomized maze using the DFS algorithm to ensure complexity and solvability.
Pathfinding Algorithms: Implement DFS and UCS algorithms to find paths from a start point to a goal within the maze.
Visualization: Visual representation of the maze, the search process, and the found path using matplotlib for an intuitive understanding of how the algorithms work.
## Getting Started

### Prerequisites
Ensure you have the following installed:

Python 3.6 or higher
Matplotlib library
Numpy library
You can install the required libraries using pip:

pip install matplotlib numpy
### Installation
1. Clone the repository:

git clone https://github.com/your-username/maze-solver-project.git
cd maze-solver-project
2. Generate the Maze:
Run the maze generation script to create a new maze and save it to a file:

python maze_matrix_generator.py
This will generate a maze_matrix.txt file that represents the maze, with the start and goal positions.

3. Solve the Maze:
Run the maze solving script, specifying the pathfinding algorithm (DFS or UCS) you wish to use:

python maze.py
## Usage

1. Generating a Maze
The maze_matrix_generator.py script uses DFS to generate a random maze. You can modify the rows and columns variables in the script to adjust the maze's size.

2. Solving the Maze
The maze.py script reads the generated maze from maze_matrix.txt and solves it using either DFS or UCS, as specified. It then visualizes the maze, the search process, and the path found.

## How It Works

1. Maze Generation
The maze is generated using a DFS algorithm that randomly selects adjacent cells to visit and carves out paths between them, ensuring a solvable maze is created.

2. Maze Solving
DFS Algorithm: Explores as far as possible along each branch before backtracking. It's implemented recursively in this project.
UCS Algorithm: Explores paths in order of their cumulative cost, ensuring the shortest path is found in terms of steps taken.
3. Visualization
The project uses matplotlib to visualize the maze, the exploration of the pathfinding algorithm, and the final path from start to goal. Different colors represent walls, the path, and the current position of the search.

## Contributing

Contributions to the Maze Solver Project are welcome! Whether it's reporting a bug, discussing improvements, or adding new features, your input is valued. Feel free to fork the repository and create a pull request or open an issue.

License

Distributed under the [MIT License](https://en.wikipedia.org/wiki/MIT_License). 

## Acknowledgments

Youssef AITBOUDDROUB, for the initial codebase and project idea.
Contributors and developers interested in pathfinding algorithms and maze generation.
This README provides an overview of how to get started with the Maze Solver Project, its features, and its implementation. By following the steps outlined above, you can generate mazes, apply pathfinding algorithms, and visualize the process and solutions.