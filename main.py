import pygame
import cfg
import sys

# Ikonky nabijeni turba
# Strileni
# Nepratelska raketa
# pocitac skore
# pocitac penez
# penize


class TancikClass(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_path = cfg.TANCIK_PATHS['tank']
        self.image = pygame.image.load(self.img_path)
        self.location = (600, 550)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.location
        self.speed = 0
        self.turbo = False
        self.turbo_fuel = 0
        self.turbo_charging = 0
        self.charged = True
        print('init tancik')

    def turn(self, num):
        self.speed = num

    def goTurbo(self):
        self.turbo = True
        self.charged = False
        self.speed = self.speed * 2
        self.turbo_fuel = cfg.PARAM_TURBO_FUEL

    def move(self):
        # odpocet turba
        self.__countdown_turbo()
        # nabijeni
        self.__charge_turbo()
        # pohyb
        self.__do_step()
        # prirazeni ikonky
        self.__icon()

    def __countdown_turbo(self):
        if self.turbo_fuel > 0:
            self.turbo_fuel -= 1
            if self.turbo_fuel == 0:
                self.speed = self.speed // 2
                self.turbo = False

    def __charge_turbo(self):
        if self.charged is False:
            self.turbo_charging += 1
            if self.turbo_charging == cfg.PARAM_TURBO_CHARGE:
                self.turbo_charging = 0
                self.charged = True

    def __do_step(self):
        self.rect.left += self.speed
        self.rect.left = max(0, self.rect.left)
        self.rect.left = min(850, self.rect.left)

    def __icon(self):
        if self.speed < 0:
            self.img_path = cfg.TANCIK_PATHS['tankl']
            if self.turbo:
                self.img_path = cfg.TANCIK_PATHS['tanklt']
        if self.speed > 0:
            self.img_path = cfg.TANCIK_PATHS['tankr']
            if self.turbo:
                self.img_path = cfg.TANCIK_PATHS['tankrt']
        if self.speed == 0:
            self.img_path = cfg.TANCIK_PATHS['tank']
        self.image = pygame.image.load(self.img_path)


class GroundClass(pygame.sprite.Sprite):

    def __init__(self, img_path, location):
        pygame.sprite.Sprite.__init__(self)
        self.img_path = img_path
        self.image = pygame.image.load(self.img_path)
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.topleft = self.location

class ShootClass(pygame.sprite.Sprite):

    def __init__(self, img_path, location):
        #TODO
        pygame.sprite.Sprite.__init__(self)
        self.img_path = img_path
        self.image = pygame.image.load(self.img_path)
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.topleft = self.location


def updateFrame(screen, tancik):
    screen.fill(cfg.COLOR_SKY)
    paintGrass(screen)
    paintTurbo(screen, tancik)
    screen.blit(tancik.image, tancik.rect)
    pygame.display.update()


def paintTurbo(screen, tancik):
    if tancik.charged is True:
        img_path = cfg.ICON_PATHS['turbo']
        location = [850, 600]
        turbo = GroundClass(img_path, location)
        icons = pygame.sprite.Group()
        icons.add(turbo)
        icons.draw(screen)


def paintGrass(screen):
    grounds = pygame.sprite.Group()

    for i in range(cfg.WIDTH // cfg.TILE_SIZE):
        location = [i * cfg.TILE_SIZE, 600]
        img_path = cfg.LANDSCAPE_PATHS['grass1']
        ground = GroundClass(img_path, location)
        grounds.add(ground)
    grounds.draw(screen)


def ShowPlaygroundScreen(screen, tancik):
    screen.fill(cfg.COLOR_SKY)
    paintGrass(screen)
    screen.blit(tancik.image, tancik.rect)
    pygame.display.update()


def ShowStartInterface(screen, screensize):
    screen.fill((255, 255, 255))
    tfont = pygame.font.Font(cfg.FONTPATH, screensize[0] // 5)
    cfont = pygame.font.Font(cfg.FONTPATH, screensize[0] // 20)
    title = tfont.render(u'Tancik', True, (0, 128, 0))
    content = cfont.render(u'Press any key to start', True, (0, 200, 0))
    trect = title.get_rect()
    trect.midtop = (screensize[0] / 2, screensize[1] / 5)
    crect = content.get_rect()
    crect.midtop = (screensize[0] / 2, screensize[1] / 2)
    screen.blit(title, trect)
    screen.blit(content, crect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return
            pygame.display.update()


def main():
    pygame.init()

    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('Skier Game')
    ShowStartInterface(screen, cfg.SCREENSIZE)
    # init Tancik
    tancik = TancikClass()
    ShowPlaygroundScreen(screen, tancik)

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and tancik.turbo is False:
                    tancik.turn(-2)
                if event.key == pygame.K_RIGHT and tancik.turbo is False:
                    tancik.turn(2)
                if event.key == pygame.K_DOWN and tancik.turbo is False:
                    tancik.turn(0)
                if event.key == pygame.K_x and tancik.turbo is False and tancik.charged is True:
                    tancik.goTurbo()

        tancik.move()
        updateFrame(screen, tancik)
        clock.tick(cfg.FPS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
