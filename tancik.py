import pygame
import cfg
from upgrades import UpgradesClass
from shoot import ShootClass


class TancikClass(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_path = cfg.TANCIK_PATHS['tank']
        self.image = pygame.image.load(self.img_path)
        self.imagemove = pygame.image.load(cfg.TANCIK_PATHS['tankl'])
        self.location = (600, 550)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.location
        self.speed = 0
        self.moving = False
        self.turbo = False
        self.turbo_fuel = 0
        self.turbo_charging = 0
        self.charged = True
        self.loaded = True
        self.reload = 0
        self.upgrades = UpgradesClass()
        self.podimage = pygame.image.load(self.upgrades.speedImagePath)
        self.reloadimage = pygame.image.load(self.upgrades.reloadImagePath)
        self.powerimage = pygame.image.load(self.upgrades.powerImagePath)
        self.shoots = pygame.sprite.Group()
        print('init tancik')

    def __turn(self, num):
        self.speed = num

    def stop(self):
        self.__turn(0)

    def go_left(self):
        self.__turn(self.upgrades.get_speed() * -1)

    def go_right(self):
        self.__turn(self.upgrades.get_speed())

    def goTurbo(self):
        self.turbo = True
        self.charged = False
        self.speed = self.speed * 2
        self.turbo_fuel = cfg.PARAM_TURBO_FUEL

    def shoot_from_gun(self):
        location = self.__get_shoot_midbottom(9)
        img_path = cfg.SHOOT_PATHS['tshoot']
        shoot = ShootClass(img_path, location, self.upgrades.get_power())
        self.shoots.add(shoot)

    def __get_shoot_midbottom(self, size):
        self.reload = self.upgrades.get_reload()
        self.loaded = False
        return [self.rect.midtop[0], self.rect.midtop[1] + size]

    def set_upgrades_images(self):
        self.podimage = pygame.image.load(self.upgrades.speedImagePath)
        self.reloadimage = pygame.image.load(self.upgrades.reloadImagePath)
        self.powerimage = pygame.image.load(self.upgrades.powerImagePath)

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
        #pohyb strel
        self.__move_shoots()

    def paint_tank(self, screen):
        self.shoots.draw(screen)
        screen.blit(self.image, self.rect)
        screen.blit(self.podimage, self.rect)
        screen.blit(self.reloadimage, self.rect)
        screen.blit(self.powerimage, self.rect)
        if self.moving:
            screen.blit(self.imagemove, self.rect)

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

    def __move_shoots(self):
        for shoot in self.shoots:
            shoot.move()
            if shoot.is_too_high():
                self.shoots.remove(shoot)

    def __icon(self):
        if self.speed < 0:
            impath = cfg.TANCIK_PATHS['tankl']
            self.moving = True
            if self.turbo:
                impath = cfg.TANCIK_PATHS['tanklt']
        if self.speed > 0:
            impath = cfg.TANCIK_PATHS['tankr']
            self.moving = True
            if self.turbo:
                impath = cfg.TANCIK_PATHS['tankrt']
        if self.speed == 0:
            self.moving = False
        if self.moving == True:
            self.imagemove = pygame.image.load(impath)
