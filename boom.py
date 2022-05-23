import pygame
from pygame.sprite import Sprite


class Explosions(Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = pygame.image.load('images/boom.bmp')
        self.rect = self.image.get_rect(center=center)
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == 50:
                self.kill()
