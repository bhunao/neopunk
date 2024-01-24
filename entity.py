import pygame
from dataclasses import dataclass


@dataclass
class Entity:
    x: int = 0
    y: int = 0
    speedx: int = 0
    speedy: int = 0

    def draw(self, screen, rect=None):
        color = (255, 0, 0)
        if rect is None:
            rect = (self.x, self.y, 25, 25)
        pygame.draw.rect(screen, color, rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speedx
        if keys[pygame.K_RIGHT]:
            self.x += self.speedx
        if keys[pygame.K_UP]:
            self.y -= self.speedy
        if keys[pygame.K_DOWN]:
            self.y += self.speedy


@dataclass
class StaticEntity:
    x: int = 0
    y: int = 0

    def draw(self, screen, rect=None):
        color = (255, 255, 0)
        if rect is None:
            rect = (self.x, self.y, 25, 25)
        pygame.draw.rect(screen, color, rect)

    def update(self):
        pass
