import pygame
import cfg
import sys


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
