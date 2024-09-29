import pygame
import math
from queue import PriorityQueue
import time

# width of the window
WIDTH = 800
pygame.init()
# Start Window
WIN = pygame.display.set_mode((WIDTH , WIDTH)) 
# Set Caption to see
pygame.display.set_caption("A* Path Finding Algorithm") 


# Define colors
LIGHT_BLUE = (0 , 102 , 204) # for start point
GREEN = (0 , 255 , 0) # for end point
LIGHT_GREEN = (0 , 204, 0) # for shortest path (after finding)
YELLOW = (255, 255 , 51) # for visited nodes
LIGHT_ORANGE = (255, 153 , 51) # for unvisited nodes
BLUE = (102 , 255 , 102) # for final path
WHITE = (255, 255 , 255) # for path (valid route Not walls)
BLACK = (0, 0 , 0) # for walls
GREY = (160, 160, 160) # for grid lines



class Node:
    # constructor
    def __init__(self , row , col , width , total_rows):
        self.row = row 
        self.col = col
        # find the coordinate from row and col
        self.x = row * width
        self.y= col * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    # Return the coordinated of the point
    def get_pos(self):
        return self.row , self.col
    
    # check differnet states of a node
    def is_visited(self):
        return self.color == LIGHT_ORANGE
    
    def is_open(self):
        return self.color == YELLOW
    
    def is_wall(self):
        return self.color == BLACK  

    def is_start(self):
        return self.color == LIGHT_BLUE
    
    def is_end(self):
        return self.color == LIGHT_GREEN
    
    def reset(self):
        self.color = WHITE

    # Set differnt states of a node
    def make_visited(self):
        self.color = YELLOW
    
    def make_open(self):
        self.color = LIGHT_ORANGE

    def make_wall(self):
        self.color = BLACK

    def make_start(self):
        self.color = LIGHT_BLUE    

    def make_end(self):
        self.color = LIGHT_GREEN
    
    def make_path(self):
        self.color = BLUE

    # Draw rectangles for each node
    def draw(self , win):
        pygame.draw.rect(win , self.color , (self.x , self.y , self.width , self.width))

    # Update the neighbours for a node 
    def update_neighbours(self , grid):
        self.neighbours = []

        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall(): # add the neighbour below
            self.neighbours.append(grid[self.row + 1][self.col])
        
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall(): # add the neighbour above
            self.neighbours.append(grid[self.row - 1][self.col])
        
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall(): # add the neighbour to the left
            self.neighbours.append(grid[self.row][self.col + 1])
        
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall(): # add the neighbour to the right
            self.neighbours.append(grid[self.row][self.col - 1])
        
    def __lt__(self , other):
        return False


def h(p1, p2): # heuristic estimate 
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1 - y2) # Manhatten Distance
    # return ((x1-x2)**2 + (y1-y2)**2)**(1/2) # Euclidian Distance


def make_grid(rows, width): # 2d Array of nodes
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows) # initialize each node
            grid[i].append(node)

    return grid

def draw_gridlines(win, rows, width): # Draw grid lines so that we can see the differnce between nodes
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*gap) , (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0) , (j * gap , width))

def draw(win, grid, rows, width): # Draw differnt elemets of the window
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_gridlines(win, rows, width)
    pygame.display.update()


def get_cicked_pos(pos, rows, width): # Get Posotion of the mouse click
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap 

    return row, col

def reconstruct_path(came_from , current , draw): # Backtract the shotest path from the parents of differnt nodes
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def astaralgorithm(draw, grid, start, end): # A* Algorithm
    count = 0
    open_set = PriorityQueue() # openset which priotizes based on the F(n)
    open_set.put((0 , count , start))
    came_from = {} # dictionary to store the parent and child to backtrak the path ater finding the end node
    g_score = { node : float("inf") for row in grid for node in row } # G(n) as infinity for all nodes initially
    g_score[start] = 0
    f_score = { node : float("inf") for row in grid for node in row } # F(n) as infinity for all nodes initially
    f_score[start] = h(start.get_pos() , end.get_pos())

    open_set_hash = {start} # start with the start node

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quit if user clicks X button
                pygame.quit()

        current_node  = open_set.get()[2] # pop a node from the priority queue the node with smallest f(n) will be prioritised
        open_set_hash.remove(current_node) # Remove teh node from the set

        if current_node == end: # trace teh path we have taken once reaching the detination
            reconstruct_path(came_from , end , draw)
            end.make_end()
            start.make_start()
            return True

        for neighbour in current_node.neighbours: # for all the neighbpurs of the current node
            temp_g_score = g_score[current_node] + 1 # consider fixed cost 1 from one node to another
            if temp_g_score < g_score[neighbour]: # if the current node is having a shortest path 
                # updated the shortest path instead of old one (initially infinity)
                came_from[neighbour] = current_node # update parent
                g_score[neighbour] = temp_g_score # update G(n)
                f_score[neighbour] = temp_g_score + h(neighbour.get_pos() , end.get_pos()) # updated F(n)

                if neighbour not in open_set_hash: # Push the neighbour to the queue
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()
        
        draw() # draw the current state

        if current_node != start and current_node != end: # do not change teh color of start and end nodes
            current_node.make_visited()

    return False




    

def main(win, width):

    ROWS = 20 # Cahnge here to see more nodes
    grid = make_grid(ROWS, WIDTH) # Initialize grid


    start = None # start node
    end = None # end node

    run = True # run the pygame loop status
    started = False # A* lgorithm status

    while run:
        draw(win, grid, ROWS, WIDTH) # Draw initial state
        for event in pygame.event.get(): # for each event in the window
            if event.type == pygame.QUIT: # quit if user clicks X button
                run = False
            
            if started: # Do not consider usr input once the A* algorithm is started
                continue

            if pygame.mouse.get_pressed()[0]: # handle left click mouse
                pos = pygame.mouse.get_pos()
                row, col = get_cicked_pos(pos, ROWS, WIDTH)
                node = grid[row][col]

                if not start and node != end: # select start node
                    start = node
                    start.make_start()

                elif not end and node != start: # select end node
                    end = node
                    end.make_end()

                elif node != end and node != start: # selct walls
                    node.make_wall()


            elif pygame.mouse.get_pressed()[2]: # Handle mouse right click
                pos = pygame.mouse.get_pos()
                row, col = get_cicked_pos(pos, ROWS, WIDTH)
                node = grid[row][col]
                node.reset() # make other nodes wihte (valid path)

                if node == start: # reset start node
                    start = None
                elif node == end: # reset end node
                    end = None
            
            if event.type == pygame.KEYDOWN: # check for kwy board event
                if event.key == pygame.K_SPACE and not started: # if the event is space button start the algorithm
                    for row in grid: # update all the neighbours for each node
                        for node in row:
                            node.update_neighbours(grid)
                    
                    start_time = time.time()
                    astaralgorithm(lambda: draw(win, grid, ROWS, WIDTH), grid , start , end) # algorithm
                    end_time = time.time()
                    print(end_time - start_time)


    pygame.quit() # quit pygame

main(WIN , WIDTH)