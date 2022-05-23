class GameStats:
    """
    Tracking statistics for the game
    """

    def __init__(self, AlienInvasion):
        """
        statistic initialization
        :param AlienInvasion: class example
        """
        self.settings = AlienInvasion.settings
        self.reset_stats()
        # Check if game starting and in active position
        self.game_active = False
        # !!!record!!!
        self.high_score = 0

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
