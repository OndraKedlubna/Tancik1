import pygame
import cfg
import sys
from ground import GroundClass
from tancik import TancikClass
from shoot import ShootClass

# Ikonky nabijeni turba
# Strileni
# Nepratelska raketa
# pocitac skore
# pocitac penez
# penize


def create_shoot(tancik, tancik_shoots):
    location = tancik.get_shoot_midbottom(9)
    img_path = cfg.SHOOT_PATHS['tshoot']
    shoot = ShootClass(img_path, location, 5)
    tancik_shoots.add(shoot)


def moove_shoots(tancik_shoots):
    for shoot in tancik_shoots:
        shoot.move()
        if shoot.is_too_high():
            tancik_shoots.remove(shoot)


def updateFrame(screen, tancik, tancik_shoots):
    screen.fill(cfg.COLOR_SKY)
    paintGrass(screen)
    paintTurbo(screen, tancik)
    tancik_shoots.draw(screen)
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
    tancik_shoots = pygame.sprite.Group()
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
                if event.key == pygame.K_SPACE:
                    create_shoot(tancik, tancik_shoots)

        tancik.move()
        moove_shoots(tancik_shoots)
        updateFrame(screen, tancik, tancik_shoots)
        clock.tick(cfg.FPS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
