import logging
from typing import List
import pygame
from pygame.rect import Rect
from entity import Entity, MovableEntity, StaticEntity

logger = logging.getLogger(__name__)


def keyboard_movement(player: MovableEntity, collidable_enties: List[Entity]):
    keys = pygame.key.get_pressed()
    old_x = player.rect.x
    old_y = player.rect.y

    if keys[pygame.K_LEFT]:
        player.rect.x -= player.speedx
    if keys[pygame.K_RIGHT]:
        player.rect.x += player.speedx
    if keys[pygame.K_UP]:
        player.rect.y -= player.speedy
    if keys[pygame.K_DOWN]:
        player.rect.y += player.speedy
    if keys[pygame.K_SPACE] and not player.is_jumping:
        pass

    for entity in collidable_enties:
        if entity is player:
            continue
        if player.rect.colliderect(entity.rect):
            player.rect.x = old_x
            player.rect.y = old_y
            logger.warn(f"{player=} collided with {entity=}")
            return


pygame.init()

screen = pygame.display.set_mode((800, 600))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

running = True
player = MovableEntity(
        Rect(150, 150, 30, 30),
        speedx=1, speedy=1,
        color=(255, 15, 192))

ground_rect = Rect(0, 575, 800, 5)
rect_1 = Rect(150, 450, 200, 25)
rect_2 = Rect(350, 500, 200, 25)
rect_3 = Rect(650, 375, 200, 25)

BLUE = (0, 0, 255)

ground = StaticEntity(ground_rect, color=BLUE)
plataform_1 = StaticEntity(rect_1, color=BLUE)
plataform_2 = StaticEntity(rect_2, color=BLUE)
plataform_3 = StaticEntity(rect_3, color=BLUE)


entities_list = [
    player,
    ground,
    plataform_1,
    plataform_2,
    plataform_3,
]

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    keyboard_movement(player, collidable_enties=entities_list)
    for entity in entities_list:
        entity.draw(screen)
        entity.update()

    pygame.display.flip()

pygame.quit()
