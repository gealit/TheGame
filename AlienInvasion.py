import sys
from time import sleep
from random import randint
import pygame

from settigns import Settings
from gamestats import GameStats
from scoreboard import ScoreBoard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from boom import Explosions
from sounds import Sounds


class AlienInvasion:
    """
    Game resource management Class.
    """
    def __init__(self):
        """
        Game initialization and creation game resources.
        """
        pygame.init()
        self.settings = Settings()

        # settings for full screen!
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('Alien Invasion')
        # for storing the statistic
        self.stats = GameStats(self)
        self.scoreboard = ScoreBoard(self)
        self.stars = pygame.sprite.Group()
        self._draw_stars()

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.booms = pygame.sprite.Group()

        self._create_fleet()
        self.play_button = Button(self, 'Нажми, что бы начать!')
        self.sound = Sounds()

    def run_game(self):
        """
        Starting mail cycle of the game
        :return: nothing
        """
        while True:
            # Following mouse and keyboard actions
            self._check_events()
            if self.stats.game_active:

                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """
        process keyboard and mouse inputs
        :return: nothing
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """
        Starts The game in case of pushing The button
        :param mouse_pos:
        :return: nothing
        """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.sound.play_background()
            # reset settings
            self.settings.initialize_dynamic_settings()

            # reset statistics
            self.stats.reset_stats()
            self.stats.game_active = True
            self.scoreboard.prep_score()
            self.scoreboard.prep_level()
            self.scoreboard.prep_ships()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            # remove mouse
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """
        react to the pushing keys
        :param event: event
        :return: nothing
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        """
        react to release from keyboard
        :param event: event
        :return: nothing
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """
        creation new bullet and join it to the bullets.
        :return: noting
        """
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.sound.play_shot()

    def _draw_stars(self):
        """
        creation stars
        :return: nothing
        """
        for number in range(0, 100):
            new_star = Star(self)
            new_star.rect.x = randint(0, 1024)
            new_star.rect.y = randint(0, 768)
            self.stars.add(new_star)

    def _update_bullets(self):
        """
        refresh and remove bullets
        :return: nothing
        """
        self.bullets.update()
        # removing bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """
        Check collisions bullet at alien
        :return:
        """
        # if collide remove bullet and alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for alien in collisions.values():
                self.stats.score += self.settings.alien_points * len(alien)
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

        # draw collisions (boom)
        self.booms.update()

        for place in collisions:
            expl = Explosions(place.rect.center)
            self.booms.add(expl)
            self.sound.play_boom()

        if not self.aliens:
            # remove bullets and creation of new fleet
            self.sound.play_checkpoint()
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # increase lvl
            self.stats.level += 1
            self.scoreboard.prep_level()

    def _update_aliens(self):
        """
        refresh all aliens positions at the fleet
        :return: nothing
        """
        self._check_fleet_edges()
        self.aliens.update()

        # check collision between alien and ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # check aliens at the bottom
        self._check_aliens_bottom()

    def _ship_hit(self):
        """
        work with ship collision
        :return:
        """
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            self.scoreboard.prep_ships()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            self.sound.play_fail()
            sleep(1)
        else:
            self.stats.game_active = False
            self.sound.play_start()
            pygame.mouse.set_visible(True)
            self.play_button = Button(self, 'Нажми, что бы играть ещё!')

    def _check_aliens_bottom(self):
        """

        :return:
        """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        """
        reaction to the reaching the edge
        :return:
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """
        All fleet to the down and change direction.
        :return:
        """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        """
        Fleet creation
        :return: nothing
        """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Find number of the rows.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - 5 * ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

        # Creation of the first alien's line.

    def _create_alien(self, alien_number, row_number):
        """
        creation of alien and placing it in the row.
        :param alien_number: number of aliens in the row
        :return: nothing
        """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        """
        Refresh screen
        :return: nothing
        """
        # redraw the screen
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.booms.draw(self.screen)

        # score information
        self.scoreboard.show_score()

        # The button shows if the game is not active
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Showing last screen actions
        pygame.display.flip()


if __name__ == '__main__':
    # Creation and starting The game.
    ai = AlienInvasion()
    ai.run_game()
