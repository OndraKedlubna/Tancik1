import pygame
import cfg
import random
from eship import EShipClass


class InfoClass():

    def __init__(self, difficulty):
        self.level = 0
        self.score = 400
        self.multiplier = 1
        self.multiplier_time = 0
        self.difficulty = difficulty
        self.enemies_limit = 0
        self.enemies_names = []
        self.enemies = pygame.sprite.Group()

    def is_clean(self):
        if len(self.enemies) + len(self.enemies_names) == 0:
            return True

    def increase_level(self):
        if self.level == cfg.MAX_LEVEL:
            return True
        self.level += 1
        level_map = cfg.LEVELS.get(self.level)
        for enemy in level_map.keys():
            for n in range(level_map.get(enemy)):
                self.enemies_names.append(enemy)
        self.enemies_limit = cfg.ENEMIES_LIMIT.get(self.level) * self.difficulty
        return False

    def add_enemy(self):
        if len(self.enemies) < self.enemies_limit and len(self.enemies_names) > 0:
            enemy_name = random.choice(self.enemies_names)
            print('adding')
            print(str(self.enemies_names))
            self.enemies_names.remove(enemy_name)
            print(str(self.enemies_names))
            if enemy_name == 'eminion':
                self.enemies.add(EShipClass('eminion', (random.randint(0, 850), 300), 0))

    def clean_enemies(self):
        for enemy in self.enemies:
            if not enemy.is_live:
                if enemy.decrease_live():
                    self.enemies.remove(enemy)

    def decrease_score(self, amount):
        self.score = self.score - amount

    def increase_score(self, amount, multiplier):
        self.score = self.score + amount * self.multiplier
        self.increase_multiplier(multiplier)
        self.multiplier_time = 0

    def increase_multiplier(self, amount):
        self.multiplier = self.multiplier + amount
        self.multiplier = min(15, self.multiplier)

    def decrease_multiplier(self, amount):
        self.multiplier = self.multiplier - amount
        self.multiplier = max(1, self.multiplier)


