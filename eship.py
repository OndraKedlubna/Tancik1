import pygame
import cfg


class EShipClass(pygame.sprite.Sprite):

    def __init__(self, img_name, location, speed, way, shootspeed):
        pygame.sprite.Sprite.__init__(self)
        self.img_name = img_name
        self.image = pygame.image.load(cfg.ENEMIES_PATHS[img_name])
        self.location = location
        self.speed = speed
        self.shootspeed = shootspeed
        self.way = way
        self.rect = self.image.get_rect()
        self.rect.topleft = self.location
        self.live = 80
        self.is_live = True

    def die(self):
        if self.is_live:
            self.img_name = self.img_name + 'D'
            self.image = pygame.image.load(cfg.ENEMIES_PATHS[self.img_name])
            self.is_live = False
