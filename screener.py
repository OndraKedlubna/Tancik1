import pygame
import cfg
import sys
from ground import GroundClass


class ScreenerClass:

    def __init__(self):
        pass

    def show_workshop(self, tancik, screen, info):
        workshop = True
        screen.fill((255, 255, 255))

        mfont = pygame.font.Font(cfg.FONTPATH, cfg.TILE_SIZE)
        sfont = pygame.font.Font(cfg.FONTPATH, cfg.TILE_SIZE // 2)
        minfo = mfont.render("Dilna(navrat do hry stiskem w)", True, (0, 128, 0))
        minfo2 = sfont.render("Zde muzou totalne nasazeni mechanici vylepsit tvuj tank", True, (0, 128, 0))

        ## tohle dej do metody
        crect = minfo.get_rect()
        crect.midtop = (cfg.SCREENSIZE[0] / 2, cfg.TILE_SIZE)
        screen.blit(minfo, crect)

        crect = minfo2.get_rect()
        crect.midtop = (cfg.SCREENSIZE[0] / 2, cfg.TILE_SIZE * 2)
        screen.blit(minfo2, crect)


        while workshop:
            screen.fill((255, 255, 255), (0, 0, screen.get_width(), cfg.TILE_SIZE))
            self.__show_score(screen, info)
            screen.fill((255, 255, 255), (0, cfg.TILE_SIZE * 3, screen.get_width(), screen.get_height()))
            cheat = 1
            cur_speed = tancik.upgrades.speed
            cur_speed_cost = cfg.UPGRADES.get('speed').get(cur_speed).get('cost') // cheat
            cur_reload = tancik.upgrades.reload
            cur_reload_cost = cfg.UPGRADES.get('reload').get(cur_reload).get('cost') // cheat
            cur_power = tancik.upgrades.power
            cur_power_cost = cfg.UPGRADES.get('power').get(cur_power).get('cost') // cheat

            multiplier_text = mfont.render(
                "[A]Motor: %s z %d, cena %d" % (cur_speed, cfg.UPGRADES.get('speed').get('cap'),
                                                cur_speed_cost), True, (153, 102, 0))
            crect = multiplier_text.get_rect()
            crect.midtop = (cfg.SCREENSIZE[0] / 2, cfg.TILE_SIZE * 3)
            screen.blit(multiplier_text, crect)

            reload_text = mfont.render(
                "[S]Nabijeni: %s z %d, cena %d" % (cur_reload, cfg.UPGRADES.get('reload').get('cap'),
                                                cur_reload_cost), True, (153, 102, 0))
            crect = reload_text.get_rect()
            crect.midtop = (cfg.SCREENSIZE[0] / 2, cfg.TILE_SIZE * 4)
            screen.blit(reload_text, crect)

            power_text = mfont.render(
                "[D]Kanon: %s z %d, cena %d" % (cur_power, cfg.UPGRADES.get('power').get('cap'),
                                                   cur_power_cost), True, (153, 102, 0))
            crect = power_text.get_rect()
            crect.midtop = (cfg.SCREENSIZE[0] / 2, cfg.TILE_SIZE * 5)
            screen.blit(power_text, crect)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    workshop = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    if info.money >= cur_speed_cost:
                        if tancik.upgrades.upgrade_speed():
                            info.decrease_money(cur_speed_cost)
                            tancik.set_upgrades_images()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    if info.money >= cur_reload_cost:
                        if tancik.upgrades.upgrade_reload():
                            info.decrease_money(cur_reload_cost)
                            tancik.set_upgrades_images()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    if info.money >= cur_power_cost:
                        if tancik.upgrades.upgrade_power():
                            info.decrease_money(cur_power_cost)
                            tancik.set_upgrades_images()
                pygame.display.update()

    def showStartInterface(self, screen):
        screensize = cfg.SCREENSIZE
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
                    return 0
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                    return 1
                pygame.display.update()

    def ShowEndInterface(self, info, screen, win):
        screensize = cfg.SCREENSIZE
        screen.fill((255, 255, 255))
        message = u'Zemrel si hrdinskou smrti pri obrane rise'
        if win:
            message = u'Gratulace! Nepratele jsou mrtvi, vyhral jsi!'
        else:
            info.decrease_score(100)
        cfont = pygame.font.Font(cfg.FONTPATH, screensize[0] // 20)
        score = cfont.render("Konecne score: %s" % info.score, True, (0, 0, 0))
        srect = score.get_rect()
        srect.midtop = (screensize[0] / 2, screensize[1] / 5)
        screen.blit(score, srect)
        content = cfont.render(message, True, (0, 200, 0))
        crect = content.get_rect()
        crect.midtop = (screensize[0] / 2, screensize[1] *2 / 5)
        screen.blit(content, crect)
        content2 = cfont.render(u'Stisknutim klavesy Q to cele skoncis', True, (0, 200, 0))
        crect2 = content2.get_rect()
        crect2.midtop = (screensize[0] / 2, screensize[1] * 3 / 5)
        screen.blit(content2, crect2)
        content3 = cfont.render(u'Stisknutim klavesy R to zkusis znova', True, (0, 200, 0))
        crect3 = content3.get_rect()
        crect3.midtop = (screensize[0] / 2, screensize[1] * 4 / 5)
        screen.blit(content3, crect3)
        pygame.display.update()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    waiting = False
                pygame.display.update()

    def showPlaygroundScreen(self, screen, tancik, info, enemy_shoots):
        screen.fill(cfg.COLOR_SKY)
        self.__paintGrass(screen)
        self.__paintTurbo(screen, tancik)
        self.__paintShoot(screen, tancik)
        enemy_shoots.draw(screen)
        info.enemies.draw(screen)
        self.__show_score(screen, info)
        #dame to do zvlastni metody v tanku, tam se budou vykreslovat vsechny obrazky
        tancik.paint_tank(screen)
        pygame.display.update()

    def __show_score(self, screen, info, pos=(10, 10), pos2=(250, 10)):
        font = pygame.font.Font(cfg.FONTPATH, 30)
        score_text = font.render("Score: %s" % info.score, True, (0, 0, 0))
        screen.blit(score_text, pos)
        font = pygame.font.Font(cfg.FONTPATH, 30)
        multiplier_text = font.render("X%s" % info.multiplier, True, (255, 0, 0))
        screen.blit(multiplier_text, pos2)
        money_text = font.render("Valecny fond: %s" % info.money, True, (204, 154, 51))
        pos3 = (pos2[0] + 50, 10)
        screen.blit(money_text, pos3)

    def __paintTurbo(self, screen, tancik):
        if tancik.charged is True:
            img_path = cfg.ICON_PATHS['turbo']
            location = [cfg.WIDTH - cfg.TILE_SIZE * 1, cfg.HEIGHT - cfg.TILE_SIZE]
            turbo = GroundClass(img_path, location)
            icons = pygame.sprite.Group()
            icons.add(turbo)
            icons.draw(screen)

    def __paintShoot(self, screen, tancik):
        if tancik.loaded is True:
            img_path = cfg.ICON_PATHS['ishoot']
            location = [cfg.WIDTH - cfg.TILE_SIZE * 2, cfg.HEIGHT - cfg.TILE_SIZE]
            ishoot = GroundClass(img_path, location)
            icons = pygame.sprite.Group()
            icons.add(ishoot)
            icons.draw(screen)

    def __paintGrass(self, screen):
        grounds = pygame.sprite.Group()

        for i in range(cfg.WIDTH // cfg.TILE_SIZE):
            location = [i * cfg.TILE_SIZE, 600]
            img_path = cfg.LANDSCAPE_PATHS['grass1']
            ground = GroundClass(img_path, location)
            grounds.add(ground)
        grounds.draw(screen)
