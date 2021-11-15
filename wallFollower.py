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

def canMove():
    a = 1
    a

def solution(maze):
    WIN.fill(WHITE)
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 1:
                drawNode((y, x), BLACK)
                waitFor(pygame.time.get_ticks()+1)
    bounds = set([(y, x) for y in range(len(maze)) for x in range(len(maze[0]))])
    startPos = (0, 0)
    endPos = (PER_COLUMN - 1, PER_ROW - 1)
    path = [startPos]
    deadEnds = []
    while endPos not in path:
        nextFrameTime = pygame.time.get_ticks() + FRAME_LENGTH
        