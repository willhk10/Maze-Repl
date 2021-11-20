import pygame
import kruskalsMazeCreator
from customDataTypes import PriorityQueue

PER_ROW = int(input("Enter an odd width:  "))
PER_COLUMN = int(input("Enter an odd height:  "))
SQUARE_SIZE = 5
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
FRAME_LENGTH = 1

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

def nextPositions(pos, isOpenPos):
    nextPositions = []
    for move in possibleMoves:
        newPos = (pos[0] + move[0], pos[1] + move[1])
        if isOpenPos[newPos]:
            nextPositions = nextPositions + [(pos[0] + move[0], pos[1] + move[1])]
    return nextPositions

def solution(maze):
    isOpenPos = {(y, x):True for y in range(-1, PER_COLUMN + 1) for x in range(-1, PER_ROW + 1)}
    WIN.fill(WHITE)
    for y in range(-1, PER_COLUMN + 1):
        for x in range(-1, PER_ROW + 1):
            if y == -1 or y == PER_COLUMN or x == -1 or x == PER_ROW:
                isOpenPos[(y, x)] = False
            elif maze[y][x] == 1:
                drawNode((y, x), BLACK)
                isOpenPos[(y, x)] = False
                #waitFor(pygame.time.get_ticks()+1)
    nodeQueue = PriorityQueue()
    startPos = (0, 0)
    isOpenPos[startPos] = False
    endPos = (PER_COLUMN-1, PER_ROW-1)
    parentNode = {}
    nodeQueue.insert(startPos, getDistance(startPos, endPos))
    drawNode(startPos, ALIVE_COLOR)
    waitFor(pygame.time.get_ticks()+FRAME_LENGTH)
    while isOpenPos[endPos] and len(nodeQueue.items) > 0:
        nextFrameTime = pygame.time.get_ticks() + FRAME_LENGTH
        curPos = nodeQueue.popLowest()
        drawNode(curPos, DEAD_COLOR)
        for pos in nextPositions(curPos, isOpenPos):
            nodeQueue.insert(pos, getDistance(pos, endPos))
            drawNode(pos, ALIVE_COLOR)
            parentNode[pos] = curPos
            isOpenPos[pos] = False
        waitFor(nextFrameTime)
        print(f"Latency: {pygame.time.get_ticks()-(nextFrameTime)}")
    
    curNode = endPos
    while curNode in parentNode:
        drawNode(curNode, (0, 0, 255))
        waitFor(pygame.time.get_ticks() + FRAME_LENGTH)
        drawNode(parentNode[curNode], (0, 0, 255))
        curNode = parentNode[curNode]

while True:  # Infinitely generates a random maze and solves it then delays 5 seconds
    solution(kruskalsMazeCreator.generateMaze(PER_COLUMN, PER_ROW))
    waitFor(pygame.time.get_ticks() + 5000)