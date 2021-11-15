import pygame
import kruskalsMazeCreator

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
pygame.display.set_caption("Breadth First Search Maze Solving")
clock = pygame.time.Clock()  # Starts a clock
FRAME_LENGTH = 0

possibleMoves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
parentNode = {}
alivePos = []
deadPos = []


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


def nextPositions(pos, deadPos, alivePos, maze, bounds):
    global parentNode
    nextPositions = []
    for move in possibleMoves:
        newPos = (pos[0] + move[0], pos[1] + move[1])
        if newPos in bounds and not newPos in set(deadPos) and maze[newPos[0]][
                newPos[1]] != 1 and newPos not in set(alivePos):
            nextPositions = nextPositions + [
                (pos[0] + move[0], pos[1] + move[1])
            ]
            parentNode[newPos] = pos
    """"
    if pos in set(parentNode):
        if parentNode[pos] in set(parentNode):
            if parentNode[parentNode[pos]] in deadPos:
                deadPos.remove(parentNode[parentNode[pos]])
    """
    return nextPositions


def solution(maze):
    WIN.fill(WHITE)
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 1:
                drawNode((y, x), BLACK)
                delay(1)
    bounds = set([(y, x) for y in range(len(maze)) for x in range(len(maze[0]))])
    startPos = (0, 0)
    endPos = (PER_COLUMN - 1, PER_ROW - 1)
    deadPos = []
    alivePos = [startPos]
    while endPos not in alivePos and len(alivePos) > 0:
        nextFrameTime = pygame.time.get_ticks() + FRAME_LENGTH
        curPos = alivePos.pop(0)
        drawNode(curPos, DEAD_COLOR)
        deadPos = [curPos] + deadPos
        childPos = nextPositions(curPos, deadPos, alivePos, maze, bounds)
        for pos in childPos:
            drawNode(pos, ALIVE_COLOR)
        alivePos = alivePos + childPos
        waitFor(nextFrameTime)
        print(f"Latency: {pygame.time.get_ticks()-(nextFrameTime)}")

    curNode = endPos
    while curNode in parentNode:
        drawNode(curNode, (0, 0, 255))
        delay(FRAME_LENGTH)
        drawNode(parentNode[curNode], (0, 0, 255))
        curNode = parentNode[curNode]


#solution(maze1)

while True:  # Delays (waits for user to exit) infinitely
    solution(kruskalsMazeCreator.generateMaze(PER_COLUMN, PER_ROW))
    delay(5000)
