import pygame
from constants.COLORS import *

pygame.init()

size = width, height = 755, 425

boxWidth = boxHeight = 10
boxMargin = 2

screen = pygame.display.set_mode(size)
pygame.display.set_caption("A-Star Pathfinding Visualized")
continueGame = True
while continueGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continueGame = False
    screen.fill(BLACK)
    for row in range(45):
        for col in range(35):
            # Draw a grid tile
            pygame.draw.rect(screen, WHITE, [(row * boxWidth) + ((row + 1) * boxMargin),
                                             (col * boxWidth) + ((col + 1) * boxMargin),
                                             boxWidth,
                                             boxHeight])
    mouse_pos = pygame.mouse.get_pos()

    # pygame.draw.rect(screen, WHITE, [275, boxMargin, boxWidth * 5, boxHeight])
    pygame.display.flip()
pygame.quit()