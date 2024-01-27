import pygame
from pygame.sprite import Group
from pygame import font


from entity import Entity, StaticEntity, TileMap, keyboard_movement


pygame.init()

screen = pygame.display.set_mode((800, 600))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

running = True
font.init()
FONT = font.Font('freesansbold.ttf', 12)

map_dict = {f"{x} 21": "grass" for x in range(800//25)}
tilemap = TileMap(map_dict)

px, py = screen.get_rect().center
player = Entity((255, 0, 0), px, py)
groups = {
    "player": Group(),
    "tilemap": tilemap.group
}

groups["player"].add(player)


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    keyboard_movement(player)

    for group_name, group in groups.items():
        group.draw(screen)
        group.update()

    text_val = f"{player.velocity=}"
    text = FONT.render(text_val, True, (255, 255, 255))
    screen.blit(text, (0, 0))

    text_val = f"{player.rect.topleft=}"
    text = FONT.render(text_val, True, (255, 255, 255))
    screen.blit(text, (0, 15))

    pygame.display.flip()
    ppos = tilemap.pos_to_tilepos(player.pos)
    result = tilemap.check_around(ppos)
    print("cheked around:", len(tilemap.collide_with(player)))
    for t in result:
        tilemap.push_away(player, t)

pygame.quit()
