import random
import cfg
from ebase import EBaseClass


class EPlaneClass(EBaseClass):

    def __init__(self, img_name, location):
        EBaseClass.__init__(self, img_name, location)
        self.loaded = False
        self.speed_vertival_flag = False
        self.speed_vertival_target = 300
        self.way = 'down'
        self.cspeedx = self.speedx
        self.cspeedy = 0

    def move(self):
        if self.is_live:
            self.rect.left += self.cspeedx
            if self.rect.left > cfg.WIDTH + cfg.TILE_SIZE * 2:
                self.rect.left = - cfg.TILE_SIZE
                self.rect.top = random.randint(cfg.TILE_SIZE, cfg.TILE_SIZE * 8)

