import pygame
from pygame.sprite import Sprite


class Star(Sprite):

    def __init__(self, AlienInvasion):
        """
        Alien initialisation and setting start point
        :param AlienInvasion:
        """
        super().__init__()
        self.screen = AlienInvasion.screen

        # Load image and attribute rect.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # first alien appears in the up left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
