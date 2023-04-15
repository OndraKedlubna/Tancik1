import pygame
import random
import cfg
from shoot import ShootClass


class EShipClass(pygame.sprite.Sprite):

    def __init__(self, img_name, location):
        pygame.sprite.Sprite.__init__(self)
        self.img_name = img_name
        self.image = pygame.image.load(cfg.ENEMIES_PATHS[img_name])
        self.location = location
        self.speedx = cfg.ENEMIES[img_name]['speedx']
        self.speedy = cfg.ENEMIES[img_name]['speedy']
        self.reload = cfg.ENEMIES[img_name]['reload']
        self.loaded = False
        self.speed_vertival_flag = False
        self.speed_vertival_target = 300
        self.way = 'down'
        self.cspeedx = random.choice((-self.speedx, self.speedx))
        self.cspeedy = 0
        self.shootspeed = cfg.ENEMIES[img_name]['shootspeed']
        self.rect = self.image.get_rect()
        self.rect.topleft = self.location
        self.live = 80
        self.is_live = True
        self.score_value = cfg.ENEMIES[img_name]['score']

    def die(self, info):
        if self.is_live:
            self.img_name = self.img_name + 'D'
            self.image = pygame.image.load(cfg.ENEMIES_PATHS[self.img_name])
            info.increase_score(self.score_value, 3)
            self.is_live = False

    def get_shoot_midtop(self, size):
        return [self.rect.midbottom[0], self.rect.midbottom[1] + size]

    def decrease_live(self):
        self.live = self.live - 1
        return self.live < 1

    def process_shoot(self):
        if self.is_live:
            self.reload = self.reload - 1
            if self.reload < 0:
                if random.randint(0, 15) > 14:
                    img_path = cfg.SHOOT_PATHS['teshoot']
                    shoot = ShootClass(img_path, self.get_shoot_midtop(9), -self.shootspeed)
                    self.reload = self.reload = cfg.ENEMIES[self.img_name]['reload']
                    return shoot
        return None

    def move(self):
        if self.is_live:
            if not self.speed_vertival_flag:
                self.rect.left += self.cspeedx
                self.rect.left = max(0, self.rect.left)
                self.rect.left = min(cfg.WIDTH - cfg.TILE_SIZE, self.rect.left)
                if self.rect.left == 0 or self.rect.left == cfg.WIDTH - cfg.TILE_SIZE:
                    self.speed_vertival_flag = True
                    self.speed_vertival_target = random.randint(0, 400) + 50
                    if self.rect.top > self.speed_vertival_target:
                        self.way = 'up'
                        self.cspeedy = -self.speedy
                    else:
                        self.way = 'down'
                        self.cspeedy = self.speedy
                    self.cspeedx = - self.cspeedx
            else:
                self.rect.top += self.cspeedy
                if self.way == 'down':
                    self.rect.top = min(self.speed_vertival_target, self.rect.top)
                else:
                    self.rect.top = max(self.speed_vertival_target, self.rect.top)
                if self.rect.top == self.speed_vertival_target:
                    self.speed_vertival_flag = False

