import pygame.font


class Button:
    def __init__(self, AlienInvasion, msg):
        """
        Button initialisation
        :param AlienInvasion: is the class sample
        :param msg: text in the button
        """
        self.screen = AlienInvasion.screen
        self.screen_rect = self.screen.get_rect()

        # The button
        self.width, self.height = 450, 50
        self.button_color = (0, 100, 100)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(name='None', size=40)

        # Creation the image of the button and placing it in the center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """
        Converts the msg to a rectangle and aligns the text to the center
        :param msg: message
        :return: nothing
        """
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """
        Displaying an empty button and displaying a message
        :return: nothing
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
