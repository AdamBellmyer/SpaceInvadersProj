import pygame as pg
from vector import Vector
from pygame.sprite import Sprite, Group
from timer import Timer

class AlienLasers:
    def __init__(self, game):
        self.game = game
        self.stats = game.stats
        self.screen = game.screen
        self.sound = game.sound
        self.alien_lasers = Group()
        self.screen_rect = self.screen.get_rect()
        self.ship = game.ship

    def add(self, alien_laser):
        self.alien_lasers.add(alien_laser)

    def empty(self):
        self.alien_lasers.empty()

    def fire(self, alien):
        new_laser = AlienLaser(self.game, alien=alien)
        self.alien_lasers.add(new_laser)

    def update(self):
        for alien_laser in self.alien_lasers.copy():
            if alien_laser.rect.top >= 800: self.alien_lasers.remove(alien_laser)

        for alien_laser in self.alien_lasers:
            alien_laser.update()

    def draw(self):
        for alien_laser in self.alien_lasers:
            alien_laser.draw()




class AlienLaser(Sprite):
    def __init__(self, game, alien):
        super().__init__()
        # print("Exist!")
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.w, self.h = self.settings.laser_width, self.settings.laser_height
        self.ship = game.ship
        self.alien = alien
        self.color = (255, 0, 0)

        self.rect = pg.Rect(0, 0, self.w, self.h)
        # self.rect.x, self.rect.y = self.ul.x, self.ul.y
        self.center = Vector(self.alien.rect.x, self.alien.rect.y)

        self.v = Vector(0, 1) * self.settings.laser_speed_factor

        self.image_list = [pg.transform.rotozoom(pg.image.load(f'images/alienLaser_{n}.png'), 0, 0.25) for n in
                           range(2)]
        self.timer = Timer(image_list=self.image_list, delay=500, is_loop=True)

    def update(self):
        self.center += self.v
        self.rect.x, self.rect.y = self.center.x, self.center.y
        # if self.rect.colliderect(self.ship.rect):
        #     self.ship.hit()


    def draw(self): pg.draw.rect(self.screen, color=self.color, rect=self.rect)
