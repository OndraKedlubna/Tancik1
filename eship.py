import pygame


class EShipClass(pygame.sprite.Sprite):

    def __init__(self, img_path, location, speed, way, shootspeed):
        pygame.sprite.Sprite.__init__(self)
        self.img_path = img_path
        self.image = pygame.image.load(self.img_path)
        self.location = location
        self.speed = speed
        self.shootspeed = shootspeed
        self.way = way
        self.rect = self.image.get_rect()
        self.rect.topleft = self.location