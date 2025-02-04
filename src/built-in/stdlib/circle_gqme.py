import math
import sys
import time

import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

black = (0, 0, 0)
white = (255, 255, 255)

center = (width // 2, height // 2)
radius = 250  # Durchmesser = 500

points = []
for angle in range(0, 360, 10):
    # Das Pygame Koordinatensystem ist x nach Rechts, aber y nach Unten.
    x = int(math.cos(math.radians(angle)) * radius) + center[0]
    y = -int(math.sin(math.radians(angle)) * radius) + center[1]
    points.append((x, y))

for i in range(2, len(points)):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    screen.fill(black)

    pygame.draw.lines(screen, white, True, points[0:i], 2)
    pygame.display.flip()
    time.sleep(1)

pygame.quit() 