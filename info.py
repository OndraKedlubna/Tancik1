import pygame
import cfg
import random
from eship import EShipClass


class InfoClass():

    def __init__(self):
        self.level = 0
        self.enemies_limit = 0
        self.enemies_names = []
        self.enemies = pygame.sprite.Group()

    def is_clean(self):
        if len(self.enemies) + len(self.enemies_names) == 0:
            return True

    def increase_level(self):
        self.level += 1
        level_map = cfg.LEVELS.get(self.level)
        for enemy in level_map.keys():
            for n in range(level_map.get(enemy)):
                self.enemies_names.append(enemy)
        self.enemies_limit = cfg.ENEMIES_LIMIT.get(self.level)

    def add_enemy(self):
        if len(self.enemies) < self.enemies_limit and len(self.enemies_names) > 0:
            enemy_name = random.choice(self.enemies_names)
            print(str(self.enemies_names))
            self.enemies_names.remove(enemy_name)
            print(str(self.enemies_names))
            if enemy_name == 'eminion':
                self.enemies.add(EShipClass('eminion', (600, 300), 0, 0, 0))
