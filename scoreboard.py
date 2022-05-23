import pygame.font
from pygame.sprite import Group

from ship import Ship


class ScoreBoard:
    """
    Output the game information
    """
    def __init__(self, AlienInvasion):
        """
        Initializes scoring attributes
        :param AlienInvasion: class sample
        """
        self.alieninvasion = AlienInvasion
        self.screen = AlienInvasion.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = AlienInvasion.settings
        self.stats = AlienInvasion.stats

        # font settings
        self.text_color = (150, 220, 220)
        self.font = pygame.font.SysFont(None, 25)

        # initial image preparing
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        """
        Ships
        :return:
        """
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.alieninvasion)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_level(self):
        """
        Shows level
        :return: nothing
        """
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str + ' - уровень',
            True,
            self.text_color,
            self.settings.bg_color
        )

        # Output the score at up-right corner of the screen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_score(self):
        """
        Converts the current score into a graphic image
        :return: nothing
        """
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)

        self.score_image = self.font.render(
            score_str + ' - Текущий счет',
            True,
            self.text_color,
            self.settings.bg_color
        )

        # Output the score at up-right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10

    def prep_high_score(self):
        """
        Converts the current record into a graphic image
        :return: nothing
        """
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)

        self.high_score_image = self.font.render(
            high_score_str + ' - Рекорд',
            True,
            self.text_color,
            self.settings.bg_color
        )

        # Output the score at the up-mid part of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """
        check for new record
        :return: nothing
        """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """
        Shows the score at the screen
        :return: nothing
        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
