import pygame
import cfg


class TancikClass(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_path = cfg.TANCIK_PATHS['tank']
        self.image = pygame.image.load(self.img_path)
        self.location = (600, 550)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.location
        self.speed = 0
        self.turbo = False
        self.turbo_fuel = 0
        self.turbo_charging = 0
        self.charged = True
        self.loaded = True
        self.reload = 0
        print('init tancik')

    def turn(self, num):
        self.speed = num

    def goTurbo(self):
        self.turbo = True
        self.charged = False
        self.speed = self.speed * 2
        self.turbo_fuel = cfg.PARAM_TURBO_FUEL

    def get_shoot_midbottom(self, size):
        self.reload = 40
        self.loaded = False
        return [self.rect.midtop[0], self.rect.midtop[1] + size]

    def move(self):
        # nabijeni
        self.__reloading()
        # odpocet turba
        self.__countdown_turbo()
        # nabijeni
        self.__charge_turbo()
        # pohyb
        self.__do_step()
        # prirazeni ikonky
        self.__icon()

    def __reloading(self):
        if self.reload > 0:
            self.reload -= 1
            if self.reload == 0:
                self.loaded = True

    def __countdown_turbo(self):
        if self.turbo_fuel > 0:
            self.turbo_fuel -= 1
            if self.turbo_fuel == 0:
                self.speed = self.speed // 2
                self.turbo = False

    def __charge_turbo(self):
        if self.charged is False:
            self.turbo_charging += 1
            if self.turbo_charging == cfg.PARAM_TURBO_CHARGE:
                self.turbo_charging = 0
                self.charged = True

    def __do_step(self):
        self.rect.left += self.speed
        self.rect.left = max(0, self.rect.left)
        self.rect.left = min(cfg.WIDTH - cfg.TILE_SIZE, self.rect.left)

    def __icon(self):
        if self.speed < 0:
            self.img_path = cfg.TANCIK_PATHS['tankl']
            if self.turbo:
                self.img_path = cfg.TANCIK_PATHS['tanklt']
        if self.speed > 0:
            self.img_path = cfg.TANCIK_PATHS['tankr']
            if self.turbo:
                self.img_path = cfg.TANCIK_PATHS['tankrt']
        if self.speed == 0:
            self.img_path = cfg.TANCIK_PATHS['tank']
        self.image = pygame.image.load(self.img_path)
