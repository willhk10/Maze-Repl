# Manual Maze Creator
# Alden Dent
# 11/8/21

import pygame

PER_ROW = int(input("Enter width: "))
PER_COLUMN = int(input("Enter height: "))
maze = [[0 for i in range(PER_ROW)] for j in range(PER_COLUMN)]
SQUARE_SIZE = 10
WIDTH, HEIGHT = SQUARE_SIZE*PER_ROW, SQUARE_SIZE*PER_COLUMN
BLOCK_SIZE_OFFSET = .5
BLOCK_SIZE = SQUARE_SIZE - 2*BLOCK_SIZE_OFFSET

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Manual Maze Creator")  # Titles window "Snake Game"
clock = pygame.time.Clock()  # Starts a clock
FRAME_LENGTH = 90

def drawWin():
    WIN.fill(WHITE)
    for y in range(PER_COLUMN):
        for x in range(PER_ROW):
            if maze[y][x] == 1:
                pygame.draw.rect(WIN, BLACK, pygame.Rect(x*SQUARE_SIZE + BLOCK_SIZE_OFFSET, y*SQUARE_SIZE + BLOCK_SIZE_OFFSET, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()



while True:
    drawWin()
    nextFrameTime = pygame.time.get_ticks() + FRAME_LENGTH
    while pygame.time.get_ticks() < nextFrameTime:
        keys_pressed = pygame.key.get_pressed()  # Gets the keys pressed
        if keys_pressed[pygame.K_ESCAPE]:  # Quits if the escape key is pressed
            pygame.quit()
            exit()
        for event in pygame.event.get():  # Quits if window is closed
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 2:
                    print(maze)
        mouse_buttons = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        if mouse_buttons[0]:
            if 0 <= mousePos[0] < WIDTH-1 and 0 <= mousePos[1] < HEIGHT-1:
                maze[(mousePos[1]+1)//SQUARE_SIZE][(mousePos[0]+1)//SQUARE_SIZE] = 1
        if mouse_buttons[2]:
            if 0 <= mousePos[0] < WIDTH-1 and 0 <= mousePos[1] < HEIGHT-1:
                maze[(mousePos[1]+1)//SQUARE_SIZE][(mousePos[0]+1)//SQUARE_SIZE] = 0