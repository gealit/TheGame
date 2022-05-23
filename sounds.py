import pygame
from time import sleep


class Sounds:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.mixer.init()
        self.boom = pygame.mixer.Sound('./sounds/boom.mp3')
        self.shot = pygame.mixer.Sound('./sounds/shot.mp3')
        self.checkpoint = pygame.mixer.Sound('./sounds/check_point.mp3')
        self.background = pygame.mixer.Sound('./sounds/background.mp3')
        self.start = pygame.mixer.Sound('./sounds/start.mp3')
        self.fail = pygame.mixer.Sound('./sounds/fail.mp3')

        self.play_start()

    def play_boom(self):
        pygame.mixer.Channel(1).play(self.boom)

    def play_shot(self):
        pygame.mixer.Channel(2).play(self.shot)

    def play_checkpoint(self):
        pygame.mixer.Channel(3).play(self.checkpoint)

    def play_start(self):
        pygame.mixer.Channel(4).play(self.start, 1, -1)
        pygame.mixer.Channel(4).set_volume(0.3)

    def play_background(self):
        pygame.mixer.Channel(4).play(self.background, -1)
        pygame.mixer.Channel(4).set_volume(0.5)

    def play_fail(self):
        pygame.mixer.Channel(5).play(self.fail)







