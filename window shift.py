import pygame
import random
import os

pygame.init()

os.environ["SDL_VIDEO_CENTERED"] = "1"
running = True
while running:
    pygame.time.delay(500)
    x = random.randrange(500)
    y = random.randrange(500)
    if not x and not y:running = False
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen = pygame.display.set_mode((x,y))
        screen.fill((random.randrange(256), random.randrange(256), random.randrange(256)))
        pygame.display.flip()

