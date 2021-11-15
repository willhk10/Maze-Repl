#http://weblog.jamisbuck.org/2011/1/3/maze-generation-kruskal-s-algorithm

import random


isMain = __name__ == "__main__"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FRAME_LENGTH = 20

if isMain:
    import pygame

    PER_COL = int(input("Enter an odd height"))
    PER_ROW = int(input("Enter an odd width"))
    SQUARE_SIZE = 10
    WIDTH, HEIGHT = SQUARE_SIZE * PER_ROW, SQUARE_SIZE * PER_COL
    BLOCK_SIZE_OFFSET = 0
    BLOCK_SIZE = SQUARE_SIZE - 2 * BLOCK_SIZE_OFFSET
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Foobar 3 Maze")
    clock = pygame.time.Clock()  # Starts a clock

def drawNode(node, color):
    if isMain:
        pygame.draw.rect(WIN, color, pygame.Rect(node[1] * SQUARE_SIZE + BLOCK_SIZE_OFFSET,node[0] * SQUARE_SIZE + BLOCK_SIZE_OFFSET, BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.update()

def delay(t):
    if isMain:
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

def findRoot(node, listNode):
    curNode = node
    while curNode in listNode:
        curNode = listNode[curNode]
    return curNode

def generateMaze(perCol, perRow):
    if isMain:
        WIN.fill(WHITE)
    maze = [[0 for i in range(perRow)] for j in range(perCol)]
    parentNode = {}
    edgeBag = []
    for y in range(perCol):
        for x in range(perRow):
            if x % 2 == 1 and y % 2 == 1:
                maze[y][x] = 1
                drawNode((y, x), BLACK)
                delay(0)
            elif x % 2 == 1 or y % 2 == 1:
                maze[y][x] = 1
                edgeBag.append((y, x))
                drawNode((y, x), BLACK)
                delay(0)

    while len(edgeBag) > 0:
        drawnEdge = edgeBag.pop(random.randrange(len(edgeBag)))
        if drawnEdge[0] % 2 == 1:
            borderSpace1 = (drawnEdge[0]+1, drawnEdge[1])
            borderSpace2 = (drawnEdge[0]-1, drawnEdge[1])
        if drawnEdge[1] % 2 == 1:
            borderSpace1 = (drawnEdge[0], drawnEdge[1]-1)
            borderSpace2 = (drawnEdge[0], drawnEdge[1]+1)
        root1 = findRoot(borderSpace1, parentNode)
        root2 = findRoot(borderSpace2, parentNode)
        if root1 != root2:
            parentNode[root1] = drawnEdge
            parentNode[root2] = drawnEdge
            maze[drawnEdge[0]][drawnEdge[1]] = 0
            drawNode((drawnEdge[0], drawnEdge[1]), WHITE)
            delay(FRAME_LENGTH)
    return maze



while isMain:
    generateMaze(PER_COL, PER_ROW)
    delay(500000)