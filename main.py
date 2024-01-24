import pygame
from entity import Entity, Pos, Speed, StaticEntity


pygame.init()

screen = pygame.display.set_mode((800, 600))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

running = True
one = Entity(speed=Speed(1, 1))
static_entity = StaticEntity(Pos(50, 50))

entities_list = [
        one,
        static_entity
        ]

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    for entity in entities_list:
        entity.draw(screen)
        entity.update()

    pygame.display.flip()

pygame.quit()
