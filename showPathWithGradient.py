import pygame
import random
h = 30
w = 30
list1 = [0,0,0,0,1]


maze1 = [[(random.choice(list1)) for i in range(w)] for i in range(h)]
maze1[0][1] = 0
maze1[1][0] = 0
maze1[h-1][w-1] = 0
print(maze1)
'''
maze1 = [[0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1], [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0], [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]]
'''

PER_ROW = len(maze1[0])
PER_COLUMN = len(maze1)
SQUARE_SIZE = 20
WIDTH, HEIGHT = SQUARE_SIZE * PER_ROW, SQUARE_SIZE * PER_COLUMN
BLOCK_SIZE_OFFSET = 1.5
BLOCK_SIZE = SQUARE_SIZE - 2 * BLOCK_SIZE_OFFSET

WHITE = (255, 255, 255)
REACHED_COLOR = (100, 100, 100)
ALIVE_COLOR = (255, 0, 0)
BLACK = (0, 0, 0)
TEXT_COLOR = (46, 127, 255)
DEATH_SCREEN_COLOR = BLACK

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Foobar 3 Maze")
clock = pygame.time.Clock()  # Starts a clock
FRAME_LENGTH = 60

def delay(t):
    nextFrameTime = pygame.time.get_ticks() + t
    while pygame.time.get_ticks() < nextFrameTime:
        keys_pressed = pygame.key.get_pressed()  # Gets the keys pressed
        if keys_pressed[pygame.K_ESCAPE]:  # Quits if the escape key is pressed
            pygame.quit()
            exit()
        for event in pygame.event.get():  # Quits if window is closed
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
E = 255
J = 255
K = 0
def drawWin(maze, movePos, reachedPos):
    global E
    global K
    global J
    WIN.fill(WHITE)
    for y in range(PER_COLUMN):
        for x in range(PER_ROW):
            if maze[y][x] == 1:
                pygame.draw.rect(
                    WIN, BLACK,
                    pygame.Rect(x * SQUARE_SIZE + BLOCK_SIZE_OFFSET,
                                y * SQUARE_SIZE + BLOCK_SIZE_OFFSET,
                                BLOCK_SIZE, BLOCK_SIZE))
    for pos in movePos:
        E = E - 2
        J = J - 2
        K = K + 2 
        if E < 2 or J < 2 or K > 253:
            E = 255
            J = 255
            K = 0
        pygame.draw.rect(
            WIN, (J, K, E), 
            pygame.Rect(pos[1] * SQUARE_SIZE + BLOCK_SIZE_OFFSET,
                        pos[0] * SQUARE_SIZE + BLOCK_SIZE_OFFSET, BLOCK_SIZE,
                        BLOCK_SIZE))
    for pos in reachedPos:
        pygame.draw.rect(
            WIN, REACHED_COLOR,
            pygame.Rect(pos[1] * SQUARE_SIZE + BLOCK_SIZE_OFFSET,
                        pos[0] * SQUARE_SIZE + BLOCK_SIZE_OFFSET, BLOCK_SIZE,
                        BLOCK_SIZE))
    pygame.display.update()

def drawNode(node, color):
    pygame.draw.rect(WIN, color, pygame.Rect(node[1] * SQUARE_SIZE + BLOCK_SIZE_OFFSET,node[0] * SQUARE_SIZE + BLOCK_SIZE_OFFSET, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()

possibleMoves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
parentNode = {}


def findNextPositions(positionsToMoveFrom, reachedPositions, maze, bounds):
    global parentNode
    nextPositions = []
    for pos in positionsToMoveFrom:
        for move in possibleMoves:
            newPos = (pos[0] + move[0], pos[1] + move[1])
            if newPos in bounds and not newPos in reachedPositions and maze[newPos[0]][newPos[1]] != 1 and newPos not in nextPositions:
                nextPositions = nextPositions + [(pos[0] + move[0], pos[1] + move[1])]
                parentNode[newPos] = pos
    return nextPositions


def solution(maze):
    shortestPath = 10000000
    bounds = [(y, x) for y in range(len(maze)) for x in range(len(maze[0]))]
    startPos = (0, 0)
    endPos = (len(maze) - 1, len(maze[0]) - 1)
    reachedPositions = []
    positionsToMoveFrom = [startPos]
    tempPathLength = 1
    while endPos not in reachedPositions and len(positionsToMoveFrom) > 0:
        drawWin(maze, positionsToMoveFrom, reachedPositions)
        delay(FRAME_LENGTH)
        reachedPositions = reachedPositions + positionsToMoveFrom
        #print(f"Number of heads: {len(positionsToMoveFrom)}")
        #print(positionsToMoveFrom)
        #print()
        positionsToMoveFrom = findNextPositions(positionsToMoveFrom, reachedPositions, maze, bounds)
        tempPathLength = tempPathLength + 1
        #print(f"Time difference is: {nextFrameTime - pygame.time.get_ticks()}")
    if tempPathLength < shortestPath and len(positionsToMoveFrom) > 0:
        shortestPath = tempPathLength
    return shortestPath


print('yes,', solution(maze1))




curNode = (PER_COLUMN-1, PER_ROW-1)
shortestPath = [curNode]
while curNode in parentNode:
    curNode = parentNode[curNode]
    shortestPath.append(curNode)
print(shortestPath) #lmfaoooo 
B = 255
G = 127.5
R = 0
for pos in shortestPath:
    B = B - (255/(len(shortestPath)))
    R = R + (255/(len(shortestPath)))
    G = G - (255/(len(shortestPath)))/2
    drawNode(pos, (R, G, B)) 
    delay(FRAME_LENGTH)

while True:
    keys_pressed = pygame.key.get_pressed()  # Gets the keys pressed
    if keys_pressed[pygame.K_ESCAPE]:  # Quits if the escape key is pressed
        pygame.quit()
        exit()
    for event in pygame.event.get():  # Quits if window is closed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
