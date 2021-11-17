import pygame
import random
import cfg


class EShipClass(pygame.sprite.Sprite):

    def __init__(self, img_name, location, shootspeed):
        pygame.sprite.Sprite.__init__(self)
        self.img_name = img_name
        self.image = pygame.image.load(cfg.ENEMIES_PATHS[img_name])
        self.location = location
        self.speedx = cfg.ENEMIES[img_name]['speedx']
        self.speedy = cfg.ENEMIES[img_name]['speedy']
        self.cspeedx = random.choice((-self.speedx, self.speedx))
        self.shootspeed = shootspeed
        self.rect = self.image.get_rect()
        self.rect.topleft = self.location
        self.live = 80
        self.is_live = True

    def die(self):
        if self.is_live:
            self.img_name = self.img_name + 'D'
            self.image = pygame.image.load(cfg.ENEMIES_PATHS[self.img_name])
            self.is_live = False

    def decrease_live(self):
        self.live = self.live - 1
        return self.live < 1

    def move(self):
        if self.is_live:
            self.rect.left += self.cspeedx
            self.rect.left = max(0, self.rect.left)
            self.rect.left = min(850, self.rect.left)
            if self.rect.left == 0 or self.rect.left == 850:
                self.cspeedx = - self.cspeedx
