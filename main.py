import pygame
import cfg
import sys
from ground import GroundClass
from tancik import TancikClass
from shoot import ShootClass
from info import InfoClass

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


def updateFrame(screen, tancik, tancik_shoots, enemies):
    screen.fill(cfg.COLOR_SKY)
    paintGrass(screen)
    paintTurbo(screen, tancik)
    paintShoot(screen, tancik)
    tancik_shoots.draw(screen)
    enemies.draw(screen)
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


def paintShoot(screen, tancik):
    if tancik.loaded is True:
        img_path = cfg.ICON_PATHS['ishoot']
        location = [800, 600]
        ishoot = GroundClass(img_path, location)
        icons = pygame.sprite.Group()
        icons.add(ishoot)
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
    content = cfont.render(u'Pro pokracovani zmackni libovolnou klavesu', True, (0, 200, 0))
    trect = title.get_rect()
    trect.midtop = (screensize[0] / 2, screensize[1] / 5)
    crect = content.get_rect()
    crect.midtop = (screensize[0] / 2, screensize[1] / 2)
    screen.blit(title, trect)
    screen.blit(content, crect)

    dif1 = cfont.render(u'Pro pokracovani zvol obtiznost', True, (0, 200, 0))
    dif2 = cfont.render(u'P - porucik Hubert Gruber', True, (0, 200, 0))
    dif3 = cfont.render(u'G - general Heinz Guderian', True, (0, 200, 0))
    d1rect = dif1.get_rect()
    d2rect = dif2.get_rect()
    d3rect = dif3.get_rect()
    d1rect.midtop = (screensize[0] / 2, screensize[1] * 6 / 9)
    d2rect.midtop = (screensize[0] / 2, screensize[1] * 7 / 9)
    d3rect.midtop = (screensize[0] / 2, screensize[1] * 8 / 9)
    screen.blit(dif1, d1rect)
    screen.blit(dif2, d2rect)
    screen.blit(dif3, d3rect)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                return 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                return 2
            pygame.display.update()


def ShowEndInterface(screen, screensize, win):
    screen.fill((255, 255, 255))
    message = u'Hanba! Znicil jsi drahy tank, prohral jsi!'
    if win:
        message = u'Gratulace! Nepratele jsou mrtvi, vyhral jsi!'
    cfont = pygame.font.Font(cfg.FONTPATH, screensize[0] // 20)
    if win:
        content = cfont.render(message, True, (0, 200, 0))
        crect = content.get_rect()
        crect.midtop = (screensize[0] / 2, screensize[1] / 2)
        screen.blit(content, crect)
    content2 = cfont.render(u'Stisknutim klavesy Q to cele skoncis', True, (0, 200, 0))
    crect2 = content2.get_rect()
    crect2.midtop = (screensize[0] / 2, screensize[1] * 3 / 4)
    screen.blit(content2, crect2)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            pygame.display.update()

def update_ships(info, tancik_shoots):
    info.add_enemy()
    for enemy in info.enemies:
        enemy.move()
    hitted_enemies = pygame.sprite.groupcollide(info.enemies, tancik_shoots, False, False)
    if len(hitted_enemies) > 0:
        for enemy in hitted_enemies:
            enemy.die()
    info.clean_enemies()


def update_level(info, screen):
    if info.is_clean():
        if info.increase_level():
            ShowEndInterface(screen, cfg.SCREENSIZE, True)



def main():
    pygame.init()

    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('Tancik')
    difficulty = ShowStartInterface(screen, cfg.SCREENSIZE)
    # init Tancik
    tancik = TancikClass()
    # promene hry
    info = InfoClass(difficulty)
    debug_time = 0
    # seznamy init
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
                if event.key == pygame.K_SPACE and tancik.loaded is True:
                    create_shoot(tancik, tancik_shoots)

        tancik.move()
        moove_shoots(tancik_shoots)
        update_ships(info, tancik_shoots)
        update_level(info, screen) #Vrat jestli je konec hry

        #TODO pocitac skore zobrazeni, nastavit skore

        updateFrame(screen, tancik, tancik_shoots, info.enemies)
        clock.tick(cfg.FPS)

        debug_time += 1
        if debug_time % 40 == 0:
            print(str(info.enemies))
            print(str(info.enemies_names))
            print('enemies_count: ' + str(len(info.enemies_names)))
            print('level: ' + str(info.level))
            print('enemies_limit: ' + str(info.level))
            print('------------------------------')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
