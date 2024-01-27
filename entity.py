from itertools import product
from typing import Any, Dict, List, Tuple
from pygame import Vector2, key, Surface, Rect
from pygame import K_LEFT, K_RIGHT, K_SPACE
from pygame.sprite import Group, Sprite


MAX_VELOCITY = 2
ACCELERATION = .1
DESACELERATION = 1
GRAVITY = .1


TILE_SIZE = 25


GRASS = Surface((TILE_SIZE, TILE_SIZE))

GRASS.fill((0, 255, 0))


class StaticEntity(Sprite):
    def __init__(self, color, x, y):
        Sprite.__init__(self)
        x *= TILE_SIZE
        y *= TILE_SIZE

        self.pos: Vector2 = Vector2(x, y)

        self.image: Surface = Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill(color)

        self.rect: Rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Entity(Sprite):
    def __init__(self, color, x, y):
        Sprite.__init__(self)

        self.pos: Vector2 = Vector2(x, y)
        self.velocity: Vector2 = Vector2()

        self.image: Surface = Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill(color)

        self.rect: Rect = self.image.get_rect()

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.pos += self.velocity
        self.rect.x = self.pos.x

        if self.pos.y > 500:
            self.velocity.y = 0
        else:
            self.velocity.y = min(3, self.velocity.y + GRAVITY)

        self.rect.y = self.pos.y
        return super().update(*args, **kwargs)


class TileMap:
    def __init__(self, tiles: Dict[str, str]) -> None:
        tiles_surfaces = {"grass": GRASS}
        self.group: Group = Group()
        self.tiles = dict()
        for str_pos, tile_name in tiles.items():
            pos = [int(x) for x in str_pos.split()]
            new_ent = StaticEntity((0, 0, 0), pos[0], pos[1])
            new_ent.image = tiles_surfaces[tile_name].copy()
            self.group.add(new_ent)
            self.tiles[(pos[0], pos[1])] = new_ent

    def pos_to_tilepos(self, pos: Vector2) -> Tuple[float, float]:
        return pos.x // TILE_SIZE, pos.y // TILE_SIZE

    def check_around(self, tile_pos: Tuple[float, float]) -> List[Entity]:
        around = product([-1, 0, 1], [-1, 0, 1])
        return_tiles = []
        for position in around:
            adjacent = tile_pos[0] + position[0], tile_pos[1] + position[1]
            if self.tiles.get(adjacent):
                return_tiles.append(self.tiles[adjacent])
        return return_tiles

    def push_away(self, pushed: Entity, pusher: Entity):
        if pushed.rect.right < pusher.rect.left:
            pushed.pos.x = pusher.rect.left - 1
        elif pushed.rect.left > pusher.rect.right:
            pushed.pos.x = pusher.rect.right + 1

        if pushed.rect.bottom < pusher.rect.top:
            pushed.pos.y = pusher.rect.top - 1
        elif pushed.rect.top > pusher.rect.bottom:
            pushed.pos.y = pusher.rect.top + 1

    def collide_with(self, entity: Entity) -> List[Entity]:
        tile_pos = self.pos_to_tilepos(entity.pos)
        tiles_collided = self.check_around(tile_pos)
        return tiles_collided


def keyboard_movement(entity: Entity):
    keys = key.get_pressed()

    if keys[K_LEFT]:
        entity.velocity.x = max(-MAX_VELOCITY, entity.velocity.x-ACCELERATION)
    elif keys[K_RIGHT]:
        entity.velocity.x = min(MAX_VELOCITY, entity.velocity.x+ACCELERATION)
    else:
        entity.velocity.x = 0

    if keys[K_SPACE]:
        entity.velocity.y = -3
