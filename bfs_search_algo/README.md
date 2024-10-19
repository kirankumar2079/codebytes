# BFS algorithm (python)

Breadth-First Search (BFS) is an algorithm for traversing or searching graph/tree data structures. It explores all the nodes at the current depth level before moving on to nodes at the next level, ensuring the shortest path is found in an unweighted graph. BFS uses a queue to keep track of nodes to visit.

### Key Concepts:
Here are the key things to know about Breadth-First Search (BFS):

### 1. Traversal Method: 
   - BFS explores a graph/data structure level by level, visiting all nodes at a current depth before moving to the next depth.
   - It uses a **queue** to manage the order of node exploration.

### 2. Starting Point:
   - BFS begins at a specified start node (or root in a tree).
   - It then visits all directly connected (neighboring) nodes.

### 3. Queue for Exploration:
   - Nodes are added to the queue when first discovered.
   - Dequeue a node, then enqueue all its unvisited neighbors.

### 4. Marking Nodes:
   - Keep track of visited nodes to avoid revisiting.
   - This can be done using a boolean array or set.

### 5. Shortest Path Guarantee:
   - BFS guarantees finding the shortest path in terms of number of edges between the starting node and any reachable node in an **unweighted graph**.

### 6. Time Complexity:
   - **O(V + E)**, where `V` is the number of vertices (nodes) and `E` is the number of edges.

### 7. Applications:
   - Finding the shortest path in unweighted graphs.
   - Level-order traversal in trees.
   - Checking graph connectivity.
   - Solving puzzles (like mazes) that can be modeled as graphs.

### How BFS Works:

1. **Initialization**:
   - Start at a given node (called the "source" or "root").
   - Use a **queue** to store nodes to be explored.
   - Mark the starting node as visited to avoid revisiting it later.

2. **Exploration**:
   - Dequeue a node from the front of the queue.
   - For each unvisited neighbor of this node:
     - Mark it as visited.
     - Add it to the queue for future exploration.
   - Repeat the process until the queue is empty.

3. **Termination**:
   - The algorithm ends when there are no more nodes left in the queue.
   - BFS guarantees that all nodes at the current level are fully explored before moving on to the next level, ensuring a breadth-wise exploration.

### Pseudocode for BFS:

```python
BFS(graph, start_node):
    # Step 1: Initialize an empty queue and a visited set
    queue = []
    visited = set()

    # Step 2: Mark the start node as visited and enqueue it
    queue.append(start_node)
    visited.add(start_node)

    # Step 3: Loop while the queue is not empty
    while queue:
        # Dequeue a node from the front of the queue
        current_node = queue.pop(0)

        # Process the current node (you can print it, etc.)
        print(current_node)

        # Step 4: For each unvisited neighbor of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                # Mark neighbor as visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)
```

### Explanation of Key Steps:

1. **Start the BFS**:
   - The algorithm begins at a given `start_node`, marks it as visited, and adds it to the queue.

2. **Main BFS Loop**:
   - While the queue is not empty, a node is dequeued, and its neighbors are checked.
   - Each unvisited neighbor is marked as visited and added to the queue for future exploration.

3. **Termination**:
   - The loop continues until all reachable nodes from the start node are explored and the queue is empty.

### Example BFS Traversal:

Given the following graph:

```
    1
   / \
  2   3
 / \
4   5
```

- Start BFS from node `1`.
- Queue: `[1]`, Visited: `{1}`
- Dequeue `1`, enqueue `2` and `3`.
- Queue: `[2, 3]`, Visited: `{1, 2, 3}`
- Dequeue `2`, enqueue `4` and `5`.
- Queue: `[3, 4, 5]`, Visited: `{1, 2, 3, 4, 5}`
- Dequeue `3`, then `4`, then `5` (no new nodes to enqueue).
- Queue is empty, BFS terminates.

This BFS process ensures that nodes are explored level by level.


However there is a even faster algorithm when it comes to searching paths which is A* search algorithm see the code [here](https://github.com/kirankumar2079/codebytes/blob/main/astar_search_algo/astar.py)
 - [Read my article on A* algorithm](https://medium.com/@kiran09082001/mastering-the-a-search-algorithm-in-python-a-real-time-visualization-guide-3c4685dfd7a7)
 - [Recommended Youtube video](https://www.youtube.com/watch?v=JtiK0DOeI4A)


### Instructions to Run:
`To run this algorithm copy / download the code in` [bfs.py](https://github.com/kirankumar2079/codebytes/blob/main/bfs_search_algo/bfs.py) `and install pygame module and in the path that has the reporsitory run "python astar.py" (cells 10 - 100 are recommended)`
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
 

  - solved maze
">

 