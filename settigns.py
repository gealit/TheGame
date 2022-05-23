from random import randint


class Settings:
    """
    Contains all game's settings
    """
    def __init__(self):
        """
        Game's static settings initialization
        """
        # screen settings
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (20, 20, 20)
        # ship settings
        # self.ship_speed = 1.5
        self.ship_limit = 2
        # bullet settings
        # self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 200, 200)
        self.bullet_allowed = 3
        # aliens settings
        # self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 means move to the right; -1 to the left
        self.fleet_direction = 1

        # acceleration rate of the game
        self.speedup_scale = 1.1
        # acceleration cost of the alien
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        Initializes settings that change during the game
        :return: noting
        """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.alien_points = 10

        # fleet_direction = 1 means move to the right; -1 to the left
        self.fleet_direction = 1

    def increase_speed(self):
        """
        Increase speed settings
        :return: nothing
        """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

