import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """
    Ship management class
    """
    def __init__(self, AlienInvasion):
        """
        Ship's initialization and sets its start point
        :param AlienInvasion: is the class sample
        """
        super().__init__()
        self.screen = AlienInvasion.screen
        self.settings = AlienInvasion.settings
        self.screen_rect = AlienInvasion.screen.get_rect()

        # load image of the ship and gets rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # motion flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Updates the position of the ship taking into account the flag
        :return: nothing
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_factor

        self.rect.x = self.x

    def blitme(self):
        """
        Draws ship in current position
        :return: nothing
        """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

