import pygame
import cfg
import sys
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


def update_tank(info, enemy_shots, tancik, screen, screener):
    hitted = pygame.sprite.spritecollide(tancik, enemy_shots, False)
    if hitted:
        screener.ShowEndInterface(info, screen, False)
        ##restart game
        return True
    return False


def update_level(info, screen, screener):
    if info.is_clean():
        if info.increase_level():
            screener.ShowEndInterface(info, screen, True)
            ##restart game
            return True
    return False

def init_game(screener):
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    # init Tancik
    tancik = TancikClass()
    difficulty = screener.showStartInterface(screen)
    # promene hry
    info = InfoClass(difficulty)
    game_time = 0
    # seznamy init
    tancik_shoots = pygame.sprite.Group()
    enemy_shoots = pygame.sprite.Group()
    return screen, tancik, info, game_time, tancik_shoots, enemy_shoots



def main():
    pygame.init()
    pygame.display.set_caption('Tancik')
    # init screener
    screener = ScreenerClass()
    screen, tancik, info, game_time, tancik_shoots, enemy_shoots = init_game(screener)

    clock = pygame.time.Clock()
    while True:
        screener.showPlaygroundScreen(screen, tancik, tancik_shoots, info, enemy_shoots)
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
        new_game = update_level(info, screen, screener)
        new_game2 = update_tank(info, enemy_shoots, tancik, screen, screener)
        #restart hry
        if new_game or new_game2:
            screen, tancik, info, game_time, tancik_shoots, enemy_shoots = init_game(screener)


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
