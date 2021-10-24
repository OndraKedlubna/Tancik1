import pygame


class ShootClass(pygame.sprite.Sprite):

    def __init__(self, img_path, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.img_path = img_path
        self.image = pygame.image.load(self.img_path)
        self.location = location
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.location

    def move(self):
        self.rect.bottom -= self.speed

    def is_too_high(self):
        return self.rect.centery < 200
