import pygame
import cfg
import sys
from ground import GroundClass
from tancik import TancikClass
from shoot import ShootClass
from info import InfoClass
from screener import ScreenerClass

# pocitac penezu
# penize


def create_shoot(tancik, tancik_shoots):
    location = tancik.get_shoot_midbottom(9)
    img_path = cfg.SHOOT_PATHS['tshoot']
    shoot = ShootClass(img_path, location, 5)
    tancik_shoots.add(shoot)


def create_enemy_shoot(enemy, enemy_shoots):
    shoot = enemy.process_shoot()
    if shoot is not None:
        enemy_shoots.add(shoot)


def moove_shoots(tancik_shoots):
    for shoot in tancik_shoots:
        shoot.move()
        if shoot.is_too_high():
            tancik_shoots.remove(shoot)


def moove_enemy_shoots(enemy_shoots):
    for shoot in enemy_shoots:
        shoot.move()
        if shoot.is_too_low():
            enemy_shoots.remove(shoot)





def show_score(screen, info, pos=(10, 10), pos2=(200, 10)):
    font = pygame.font.Font(cfg.FONTPATH, 30)
    score_text = font.render("Score: %s" % info.score, True, (0, 0, 0))
    screen.blit(score_text, pos)
    font = pygame.font.Font(cfg.FONTPATH, 30)
    multiplier_text = font.render("X%s" % info.multiplier, True, (255, 0, 0))
    screen.blit(multiplier_text, pos2)


def paintTurbo(screen, tancik):
    if tancik.charged is True:
        img_path = cfg.ICON_PATHS['turbo']
        location = [cfg.WIDTH - cfg.TILE_SIZE * 1, cfg.HEIGHT - cfg.TILE_SIZE]
        turbo = GroundClass(img_path, location)
        icons = pygame.sprite.Group()
        icons.add(turbo)
        icons.draw(screen)


def paintShoot(screen, tancik):
    if tancik.loaded is True:
        img_path = cfg.ICON_PATHS['ishoot']
        location = [cfg.WIDTH - cfg.TILE_SIZE * 2, cfg.HEIGHT - cfg.TILE_SIZE]
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


def showPlaygroundScreen(screen, tancik, tancik_shoots, info, enemy_shoots):
    screen.fill(cfg.COLOR_SKY)
    paintGrass(screen)
    paintTurbo(screen, tancik)
    paintShoot(screen, tancik)
    tancik_shoots.draw(screen)
    enemy_shoots.draw(screen)
    info.enemies.draw(screen)
    show_score(screen, info)
    screen.blit(tancik.image, tancik.rect)
    pygame.display.update()


def ShowEndInterface(info, screen, screensize, win):
    screen.fill((255, 255, 255))
    message = u'Hanba! Znicil jsi drahy tank, prohral jsi!'
    if win:
        message = u'Gratulace! Nepratele jsou mrtvi, vyhral jsi!'
    else:
        info.decrease_score(100)
    cfont = pygame.font.Font(cfg.FONTPATH, screensize[0] // 20)
    score = cfont.render("Konecne score: %s" % info.score, True, (0, 0, 0))
    srect = score.get_rect()
    srect.midtop = (screensize[0] / 2, screensize[1] / 4)
    screen.blit(score, srect)
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


def update_ships(info, tancik_shoots, enemy_shots):
    info.add_enemy()
    for enemy in info.enemies:
        enemy.move()
        create_enemy_shoot(enemy, enemy_shots)
    hitted_enemies = pygame.sprite.groupcollide(info.enemies, tancik_shoots, False, False)
    if len(hitted_enemies) > 0:
        for enemy, shoots in hitted_enemies.items():
            enemy.die(info)
            for shoot in shoots:
                tancik_shoots.remove(shoot)
    info.clean_enemies()


def update_tank(info, enemy_shots, tancik, screen):
    hitted = pygame.sprite.spritecollide(tancik, enemy_shots, False)
    if hitted:
        ShowEndInterface(info, screen, cfg.SCREENSIZE, False)


def update_level(info, screen):
    if info.is_clean():
        if info.increase_level():
            ShowEndInterface(info, screen, cfg.SCREENSIZE, True)



def main():
    pygame.init()

    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('Tancik')
    # init screener
    screener = ScreenerClass()
    # init Tancik
    tancik = TancikClass()
    difficulty = screener.showStartInterface(screen)
    # promene hry
    info = InfoClass(difficulty)
    game_time = 0
    # seznamy init
    tancik_shoots = pygame.sprite.Group()
    enemy_shoots = pygame.sprite.Group()
    showPlaygroundScreen(screen, tancik, tancik_shoots, info, enemy_shoots)

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_LEFT and tancik.turbo is False:
                #     tancik.turn(-2)
                # if event.key == pygame.K_RIGHT and tancik.turbo is False:
                #     tancik.turn(2)
                if event.key == pygame.K_DOWN and tancik.turbo is False:
                    tancik.turn(0)
                if event.key == pygame.K_x and tancik.turbo is False and tancik.charged is True and tancik.speed != 0:
                    tancik.goTurbo()
                if event.key == pygame.K_SPACE and tancik.loaded is True:
                    create_shoot(tancik, tancik_shoots)
                if event.key == pygame.K_w and tancik.turbo is False:
                    screener.show_workshop(screen)

        if tancik.turbo is False:
            tancik.turn(0)
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT] and tancik.turbo is False:
            tancik.turn(-2)
        if key_pressed[pygame.K_RIGHT] and tancik.turbo is False:
            tancik.turn(2)

        tancik.move()
        moove_shoots(tancik_shoots)
        moove_enemy_shoots(enemy_shoots)
        update_ships(info, tancik_shoots, enemy_shoots)
        update_level(info, screen) #Vrat jestli je konec hry
        update_tank(info, enemy_shoots, tancik, screen)

        showPlaygroundScreen(screen, tancik, tancik_shoots, info, enemy_shoots)
        clock.tick(cfg.FPS)

        game_time += 1
        info.multiplier_time = info.multiplier_time + 1
        if info.multiplier_time % 150 == 0:
            info.decrease_multiplier(1)

        if game_time % 40 == 0:
            info.decrease_score(2)
            print(str(info.enemies))
            print(str(info.enemies_names))
            print('enemies_count: ' + str(len(info.enemies_names)))
            print('level: ' + str(info.level))
            print('enemies_limit: ' + str(info.level))
            print('------------------------------')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
