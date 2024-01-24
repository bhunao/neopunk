from typing import Tuple
import pygame
from dataclasses import dataclass, field

from pygame.rect import Rect
from pygame import draw


def default_rect():
    return pygame.Rect(0, 0, 25, 25)


def rgb(offset=0):
    n = (pygame.time.get_ticks() + offset) % 255
    r = n
    g = (n + 85) % 255
    b = (n + 170) % 255
    return r, g, b



@dataclass
class Entity:
    rect: Rect = field(default_factory=default_rect)
    color: Tuple[int, int, int] = (255, 0, 0)

    def draw(self, screen):
        draw.rect(screen, self.color, self.rect)

    def update(self):
        pass


@dataclass
class StaticEntity(Entity):
    def draw(self, screen):
        r, g, b = rgb(100)

        outline_rect = self.rect.copy()
        outline_rect.x -= 2
        outline_rect.y -= 2
        outline_rect.width = self.rect.width + 4
        outline_rect.height = self.rect.height + 4

        draw.rect(screen, (r, g, b), outline_rect)
        draw.rect(screen, self.color, self.rect)

    def update(self):
        pass


@dataclass
class MovableEntity(Entity):
    speedx: int = 0
    speedy: int = 0
    gravity: int = 1
    is_jumping: bool = False

    def update(self):
        r, g, b = rgb()
        self.color = r, g, b
