import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, AlienInvasion):
        """
        Alien initialisation and setting start point
        :param AlienInvasion:
        """
        super().__init__()
        self.screen = AlienInvasion.screen
        self.settings = AlienInvasion.settings

        # Load image and attribute rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # first alien appears in the up left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # saving horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """
        Return True if reach edge
        :return: bool
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """
        move the aliens
        :return: noting
        """
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x
