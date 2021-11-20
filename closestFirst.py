import pygame
import kruskalsMazeCreator
from customDataTypes import PriorityQueue

PER_ROW = int(input("Enter an odd width:  "))
PER_COLUMN = int(input("Enter an odd height:  "))
SQUARE_SIZE = 10
WIDTH, HEIGHT = SQUARE_SIZE * PER_ROW, SQUARE_SIZE * PER_COLUMN
BLOCK_SIZE_OFFSET = 0
BLOCK_SIZE = SQUARE_SIZE - 2 * BLOCK_SIZE_OFFSET

WHITE = (255, 255, 255)
DEAD_COLOR = (100, 100, 100)
ALIVE_COLOR = (255, 0, 0)
BLACK = (0, 0, 0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Closest First Search Maze Solving")
clock = pygame.time.Clock()  # Starts a clock
FRAME_LENGTH = 10

possibleMoves = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def waitFor(t):
    while pygame.time.get_ticks() < t:
        keys_pressed = pygame.key.get_pressed()  # Gets the keys pressed
        if keys_pressed[pygame.K_ESCAPE]:  # Quits if the escape key is pressed
            pygame.quit()
            exit()
        for event in pygame.event.get():  # Quits if window is closed
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def waitForSpace():
    spacePressed = False
    while not spacePressed:
        keys_pressed = pygame.key.get_pressed()  # Gets the keys pressed
        if keys_pressed[pygame.K_ESCAPE]:  # Quits if the escape key is pressed
            pygame.quit()
            exit()
        for event in pygame.event.get():  # Quits if window is closed
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    spacePressed = True
                if event.key == pygame.K_p:
                    print(parentNode)

def drawNode(node, color):
    pygame.draw.rect(
        WIN, color,
        pygame.Rect(node[1] * SQUARE_SIZE + BLOCK_SIZE_OFFSET,
                    node[0] * SQUARE_SIZE + BLOCK_SIZE_OFFSET, BLOCK_SIZE,
                    BLOCK_SIZE))
    pygame.display.update()

def getDistance(pos, endPos):
    return (endPos[0])-pos[0] + (endPos[1])-pos[1]

def inBounds(pos):
    if -1 < pos[0] < PER_COLUMN and -1 < pos[1] < PER_ROW:
        return True
    else:
        return False

def nextPositions(pos, searchedPos, nodeQueue, maze):
    nextPositions = []
    for move in possibleMoves:
        newPos = (pos[0] + move[0], pos[1] + move[1])
        if inBounds(newPos) and not newPos in set(searchedPos) and maze[newPos[0]][newPos[1]] != 1 and newPos not in set(nodeQueue.allData):
            nextPositions = nextPositions + [(pos[0] + move[0], pos[1] + move[1])]
    return nextPositions

def solution(maze):
    WIN.fill(WHITE)
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 1:
                drawNode((y, x), BLACK)
                waitFor(pygame.time.get_ticks()+1)
    nodeQueue = PriorityQueue()
    startPos = (0, 0)
    endPos = (PER_COLUMN-1, PER_ROW-1)
    searchedNodes = []
    parentNode = {}
    nodeQueue.insert(startPos, getDistance(startPos, endPos))
    drawNode(startPos, ALIVE_COLOR)
    waitFor(pygame.time.get_ticks()+FRAME_LENGTH)
    while endPos not in searchedNodes and len(nodeQueue.items) > 0:
        print(endPos in parentNode)
        nextFrameTime = pygame.time.get_ticks() + FRAME_LENGTH
        curPos = nodeQueue.popLowest()
        drawNode(curPos, DEAD_COLOR)
        for pos in nextPositions(curPos, searchedNodes, nodeQueue, maze):
            nodeQueue.insert(pos, getDistance(pos, endPos))
            drawNode(pos, ALIVE_COLOR)
            parentNode[pos] = curPos
        searchedNodes.append(curPos)
        waitFor(nextFrameTime)
        #waitForSpace()
        #print(f"Latency: {pygame.time.get_ticks()-(nextFrameTime)}")
    
    curNode = endPos
    while curNode in parentNode:
        drawNode(curNode, (0, 0, 255))
        waitFor(pygame.time.get_ticks() + FRAME_LENGTH)
        drawNode(parentNode[curNode], (0, 0, 255))
        curNode = parentNode[curNode]

while True:  # Delays (waits for user to exit) infinitely
    solution(kruskalsMazeCreator.generateMaze(PER_COLUMN, PER_ROW))
    waitFor(pygame.time.get_ticks() + 5000)