import pygame
from dataclasses import dataclass


@dataclass
class Pos:
    x: int = 0
    y: int = 0


@dataclass
class Speed:
    x: int = 0
    y: int = 0


@dataclass
class Entity:
    pos: Pos = Pos()
    speed: Speed = Speed()

    def draw(self, screen, rect=None):
        color = (255, 0, 0)
        if rect is None:
            rect = (self.pos.x, self.pos.y, 25, 25)
        pygame.draw.rect(screen, color, rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pos.x -= self.speed.x
        if keys[pygame.K_RIGHT]:
            self.pos.x += self.speed.x
        if keys[pygame.K_UP]:
            self.pos.y -= self.speed.y
        if keys[pygame.K_DOWN]:
            self.pos.y += self.speed.y


@dataclass
class StaticEntity:
    pos: Pos = Pos()

    def draw(self, screen, rect=None):
        color = (255, 255, 0)
        if rect is None:
            rect = (self.pos.x, self.pos.y, 150, 25)
        pygame.draw.rect(screen, color, rect)

    def update(self):
        pass
