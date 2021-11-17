# Maze-Repl
Alden Dent and William Keenan's adventures through maze solving and creation algorithms

## Table of Contents
* [Kruskal's Algorithm Maze Generator](#kruskalsmazecreatorpy---kruskalls-algorithm-maze-generation) <br/>
* [Breadth First Search Maze Solver](#breadthfirstpy---breadth-first-search-maze-solver)

## [kruskalsMazeCreator.py](https://github.com/willhk10/Maze-Repl/blob/main/kruskalsMazeCreator.py) - Kruskall's Algorithm Maze Generator
This code implements Kruskall's Algorithm, as described on [this website](https://weblog.jamisbuck.org/2011/1/3/maze-generation-kruskal-s-algorithm), to generate random mazes of any size with only one path between any two points. Additionally, it visualizes the process using a Pygame window.
### How It Works:
It begins by creating a list containing the coordinates of all edges, displayed below in grey, which are between two open cells, displayed below in white.
<br/><img src="https://github.com/willhk10/Maze-Repl/blob/main/Media/kruskalsBeforeCreation.png" alt="Picture showing edges and empty cells" width="400" height="240"><br/>
It then picks edges at random and removes them if doing so doesn't connect cells which are already connected, which would lead to loops in the maze, meaning multiple paths could lead between the same two points. To efficiently determine whether two groups of cells are already connected, it uses a linked list to store and find the root of each group of cells, so if they are the same, it knows not to remove that edge since both adjacent cells are already connectd. It repeats this process untill all edges have been picked, at which point the maze is complete.
<br/><img src="https://github.com/willhk10/Maze-Repl/blob/main/Media/kruskalsInAction.gif" alt="GIF of code in action" width="400" height="240"><br/>

## [breadthFirst.py](https://github.com/willhk10/Maze-Repl/blob/main/breadthFirst.py) - Breadth First Search Maze Solver

## [manualMazeCreator.py](https://github.com/willhk10/Maze-Repl/blob/main/manualMazeCreator.py) - Manual Maze Creator
