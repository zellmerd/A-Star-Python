import sys
import pygame

pygame.init()

size = width, height = 255, 255

boxWidth = boxHeight = 20
boxMargin = 5

# Colors
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
red = 255, 0, 0
blue = 0, 0, 255

screen = pygame.display.set_mode(size)
pygame.display.set_caption("A-Star Pathfinding Visualized")
continueGame = True
while continueGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continueGame = False
    screen.fill(black)
    for i in range(10):
        pygame.draw.rect(screen, white, [i * boxWidth + boxMargin, boxMargin, boxWidth, boxHeight])
    pygame.display.flip()
pygame.quit()