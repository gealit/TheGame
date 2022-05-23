import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    Bullets from the ship.
    """
    def __init__(self, AlienInvasion):
        super().__init__()
        self.screen = AlienInvasion.screen
        self.settings = AlienInvasion.settings
        self.color = self.settings.bullet_color

        # Bullet creation in position (0, 0) and adjusting the position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = AlienInvasion.ship.rect.midtop

        # Bullet's position in float format.
        self.y = float(self.rect.y)

    def update(self):
        """
        movin the bullet to the top of the screen.
        :return: nothing
        """
        # refreshing the position in float format.
        self.y -= self.settings.bullet_speed_factor

        # refreshing the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Projectile output to the screen
        :return:
        """
        pygame.draw.rect(self.screen, self.color, self.rect)

