from typing import List, Tuple
import pygame
from dataclasses import dataclass


@dataclass
class Entity:
    pos: Tuple[int] = (0, 0)
    speed: Tuple[int] = (0, 0)

    def draw(self, screen, rect=None):
        color = (255, 0, 0)
        if rect is None:
            rect = pygame.Rect(self.pos[0], self.pos[1], 100, 100)
        pygame.draw.rect(screen, color, rect)

    def update(self):
        new_x = self.pos[0] * self.speed[0]
        new_y = self.pos[1] * self.speed[1]
        self.pos = new_x, new_y
