import random
import cfg
from ebase import EBaseClass


class EShipClass(EBaseClass):

    def __init__(self, img_name, location):
        EBaseClass.__init__(self, img_name, location)
        self.loaded = False
        self.speed_vertival_flag = False
        self.speed_vertival_target = 300
        self.way = 'down'
        self.cspeedx = random.choice((-self.speedx, self.speedx))
        self.cspeedy = 0



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

