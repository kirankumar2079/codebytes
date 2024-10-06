
# A Star algorithm (python)

The A* (A-star) algorithm is a popular pathfinding and graph traversal algorithm used to find the shortest path between two nodes. It combines the advantages of Dijkstra's algorithm (which explores all possible paths) and a greedy best-first search (which prioritizes paths that seem more promising). A* is widely used in applications such as navigation systems, AI for games, and robotics.

### Key Concepts:
1. **Heuristic Function (`h`)**: Estimates the cost to reach the goal from a given node. The accuracy of this heuristic determines the efficiency of the algorithm.
2. **Cost Function (`g`)**: Represents the exact cost to reach the current node from the start.
3. **Evaluation Function (`f`)**: The sum of `g` and `h` functions:  
   \[
   f(n) = g(n) + h(n)
   \]
   A* explores nodes with the lowest `f` values first, ensuring that it finds the optimal path.

### How A* Works:
- It starts from the initial node and explores neighbors based on the `f` score.
- The algorithm uses a priority queue to expand the most promising nodes first.
- It continues expanding nodes until it reaches the goal, ensuring that the path found is the shortest.

A* is both complete and optimal, meaning it always finds a solution if one exists, and the solution will be the shortest path. Its efficiency heavily depends on the heuristic used—if the heuristic is well-designed (admissible and consistent), A* can be extremely fast.


`To run this algorithm copy / download the code in astar.py and install pygame module and in the path that has the reporsitory run "python astar.py" (cells 10 - 100 are recommended)`
 - In the window that opened
 - click wehere you want the starting point to be (bule)
 - click where you want the end point to be (green)
 - draw walls / obstacles in the path (black)
 - click space button once you are ready
 - see the time taken to run in the console

 - Color meanings
    - Blue - Staring point  <img src="https://github.com/kirankumar2079/codebytes/blob/main/astar_search_algo/images/start.png" alt="starting suare" width="20" height="20">
    - Green - Ending point  <img src="https://github.com/kirankumar2079/codebytes/blob/main/astar_search_algo/images/end.png" alt="ending square" width="20" height="20">
    - Black - Walls / Obstacles  <img src="https://github.com/kirankumar2079/codebytes/blob/main/astar_search_algo/images/wall.png" alt="Wall squares" width="20" height="20">
    - White - Valid path  <img src="https://github.com/kirankumar2079/codebytes/blob/main/astar_search_algo/images/valid.png" alt="valid square" width="20" height="20">
    - Light Green - Shortest path found  <img src="https://github.com/kirankumar2079/codebytes/blob/main/astar_search_algo/images/path.png" alt="path square" width="20" height="20">
    - Yellow - Visited Nodes  <img src="https://github.com/kirankumar2079/codebytes/blob/main/astar_search_algo/images/visited.png" alt="visited squares" width="20" height="20">
    - Orange - Nodes in the queue which are not yet visited  <img src="https://github.com/kirankumar2079/codebytes/blob/main/astar_search_algo/images/queued.png" alt="queued squares" width="20" height="20">


 sample images
 - unsolved maze
 <img src="https://github.com/kirankumar2079/codebytes/blob/main/astar_search_algo/images/maze1.png" alt="Unsolved Maze" width="500" height="500">

  - solved maze
 <img src="https://github.com/kirankumar2079/codebytes/blob/main/astar_search_algo/images/solution1.png" alt="Solved Maze" width="500" height="500">


