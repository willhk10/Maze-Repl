import pygame
'''
maze1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
         [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
         [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
         [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
         [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
         [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
         [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
'''

maze1 = [[0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
         [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0],
         [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

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
FRAME_LENGTH = 15


def drawWin(maze, movePos, reachedPos):
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
        pygame.draw.rect(
            WIN, ALIVE_COLOR,
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


possibleMoves = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def findNextPositions(positionsToMoveFrom, reachedPositions, maze, bounds):
    nextPositions = []
    for pos in positionsToMoveFrom:
        for move in possibleMoves:
            newPos = (pos[0] + move[0], pos[1] + move[1])
            if newPos in bounds and not newPos in reachedPositions and maze[
                    newPos[0]][newPos[1]] != 1 and newPos not in nextPositions:
                nextPositions = nextPositions + [
                    (pos[0] + move[0], pos[1] + move[1])
                ]
    return nextPositions


def removeOneWall(maze):
    allMazes = []
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            tempMaze = [row[:] for row in maze]
            if maze[y][x] == 1:
                if x == 0 or y == 0 or x == len(
                        maze[0]) - 1 or y == len(maze) - 1:
                    tempMaze[y][x] = 0
                    allMazes.append(tempMaze)
                elif sum([
                        maze[y + 1][x], maze[y - 1][x], maze[y][x + 1],
                        maze[y][x - 1]
                ]) < 4:
                    tempMaze[y][x] = 0
                    allMazes.append(tempMaze)
    return allMazes


def solution(maze):
    shortestPath = 10000000
    bounds = [(y, x) for y in range(len(maze)) for x in range(len(maze[0]))]
    startPos = (0, 0)
    endPos = (len(maze) - 1, len(maze[0]) - 1)
    allMazes = removeOneWall(maze)
    for tempMaze in allMazes:
        reachedPositions = []
        positionsToMoveFrom = [startPos]
        tempPathLength = 1
        while endPos not in positionsToMoveFrom and len(
                positionsToMoveFrom) > 0:
            drawWin(tempMaze, positionsToMoveFrom, reachedPositions)
            nextFrameTime = pygame.time.get_ticks() + FRAME_LENGTH
            while pygame.time.get_ticks() < nextFrameTime:
                keys_pressed = pygame.key.get_pressed(
                )  # Gets the keys pressed
                if keys_pressed[
                        pygame.K_ESCAPE]:  # Quits if the escape key is pressed
                    pygame.quit()
                    exit()
                for event in pygame.event.get():  # Quits if window is closed
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

            reachedPositions = reachedPositions + positionsToMoveFrom
            #print(f"Number of heads: {len(positionsToMoveFrom)}")
            #print(positionsToMoveFrom)
            #print()
            positionsToMoveFrom = findNextPositions(positionsToMoveFrom,
                                                    reachedPositions, tempMaze,
                                                    bounds)
            tempPathLength = tempPathLength + 1
            #print(f"Time difference is: {nextFrameTime - pygame.time.get_ticks()}")
        if tempPathLength < shortestPath and len(positionsToMoveFrom) > 0:
            shortestPath = tempPathLength
    return shortestPath


print('yes,', solution(maze1))

while True:
    keys_pressed = pygame.key.get_pressed()  # Gets the keys pressed
    if keys_pressed[pygame.K_ESCAPE]:  # Quits if the escape key is pressed
        pygame.quit()
        exit()
    for event in pygame.event.get():  # Quits if window is closed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
