import pygame
import cfg
import sys
from ground import GroundClass


class ScreenerClass:

    def __init__(self):
        pass

    def show_workshop(self, screen):
        workshop = True
        screen.fill((255, 255, 255))

        mfont = pygame.font.Font(cfg.FONTPATH, cfg.TILE_SIZE)
        sfont = pygame.font.Font(cfg.FONTPATH, cfg.TILE_SIZE // 2)
        minfo = mfont.render("Dilna", True, (0, 128, 0))
        minfo2 = sfont.render("Zde muzou totalne nasazeni mechanici vylepsit tvuj tank", True, (0, 128, 0))

        ## tohle dej do metody
        crect = minfo.get_rect()
        crect.midtop = (cfg.SCREENSIZE[0] / 2, cfg.TILE_SIZE)
        screen.blit(minfo, crect)

        crect = minfo2.get_rect()
        crect.midtop = (cfg.SCREENSIZE[0] / 2, cfg.TILE_SIZE * 2)
        screen.blit(minfo2, crect)

        while workshop:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    workshop = False
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
                    return 1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                    return 2
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

    def showPlaygroundScreen(self, screen, tancik, tancik_shoots, info, enemy_shoots):
        screen.fill(cfg.COLOR_SKY)
        self.paintGrass(screen)
        self.paintTurbo(screen, tancik)
        self.paintShoot(screen, tancik)
        tancik_shoots.draw(screen)
        enemy_shoots.draw(screen)
        info.enemies.draw(screen)
        self.show_score(screen, info)
        screen.blit(tancik.image, tancik.rect)
        pygame.display.update()

    def show_score(self, screen, info, pos=(10, 10), pos2=(200, 10)):
        font = pygame.font.Font(cfg.FONTPATH, 30)
        score_text = font.render("Score: %s" % info.score, True, (0, 0, 0))
        screen.blit(score_text, pos)
        font = pygame.font.Font(cfg.FONTPATH, 30)
        multiplier_text = font.render("X%s" % info.multiplier, True, (255, 0, 0))
        screen.blit(multiplier_text, pos2)

    def paintTurbo(self, screen, tancik):
        if tancik.charged is True:
            img_path = cfg.ICON_PATHS['turbo']
            location = [cfg.WIDTH - cfg.TILE_SIZE * 1, cfg.HEIGHT - cfg.TILE_SIZE]
            turbo = GroundClass(img_path, location)
            icons = pygame.sprite.Group()
            icons.add(turbo)
            icons.draw(screen)

    def paintShoot(self, screen, tancik):
        if tancik.loaded is True:
            img_path = cfg.ICON_PATHS['ishoot']
            location = [cfg.WIDTH - cfg.TILE_SIZE * 2, cfg.HEIGHT - cfg.TILE_SIZE]
            ishoot = GroundClass(img_path, location)
            icons = pygame.sprite.Group()
            icons.add(ishoot)
            icons.draw(screen)

    def paintGrass(self, screen):
        grounds = pygame.sprite.Group()

        for i in range(cfg.WIDTH // cfg.TILE_SIZE):
            location = [i * cfg.TILE_SIZE, 600]
            img_path = cfg.LANDSCAPE_PATHS['grass1']
            ground = GroundClass(img_path, location)
            grounds.add(ground)
        grounds.draw(screen)
