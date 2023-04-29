import pygame
import cfg
import random
from shoot import ShootClass


class EBaseClass(pygame.sprite.Sprite):

    def __init__(self, img_name, location):
        pygame.sprite.Sprite.__init__(self)
        self.img_name = img_name
        self.image = pygame.image.load(cfg.ENEMIES_PATHS[img_name])
        self.location = location
        self.speedx = cfg.ENEMIES[img_name]['speedx']
        self.speedy = cfg.ENEMIES[img_name]['speedy']
        self.reload = cfg.ENEMIES[img_name]['reload']
        self.shootspeed = cfg.ENEMIES[img_name]['shootspeed']
        self.rect = self.image.get_rect()
        self.rect.topleft = self.location
        self.live = 80
        self.is_live = True
        self.score_value = cfg.ENEMIES[img_name]['score']
        self.cspeedx = 0
        self.cspeedy = 0

    def die(self, info):
        if self.is_live:
            self.img_name = self.img_name + 'D'
            self.image = pygame.image.load(cfg.ENEMIES_PATHS[self.img_name])
            info.increase_score(self.score_value, 3)
            self.is_live = False

    def decrease_live(self):
        self.live = self.live - 1
        return self.live < 1

    def get_shoot_midtop(self, size):
        return [self.rect.midbottom[0], self.rect.midbottom[1] + size]

    def process_shoot(self):
        if self.is_live:
            self.reload = self.reload - 1
            if self.reload < 0:
                if random.randint(0, 20) > 19:
                    img_path = cfg.SHOOT_PATHS['teshoot']
                    shoot = ShootClass(img_path, self.get_shoot_midtop(9), -self.shootspeed)
                    self.reload = self.reload = cfg.ENEMIES[self.img_name]['reload']
                    return shoot
        return None
