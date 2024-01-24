import pygame
from entity import Entity

pygame.init()


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


running = True
one = Entity(speed=[1, 0])

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    one.draw(screen)
    one.update()


    pygame.display.flip()

pygame.quit()
