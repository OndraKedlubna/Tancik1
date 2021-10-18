import pygame
import cfg
import sys


class GroundClass(pygame.sprite.Sprite):

    def __init__(self, img_path, location):
        pygame.sprite.Sprite.__init__(self)
        self.img_path = img_path
        self.image = pygame.image.load(self.img_path)
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.topleft = self.location


def updateFrame(screen):
    screen.fill(cfg.COLOR_SKY)

    paintGrass(screen)

    pygame.display.update()


def paintGrass(screen):

    grounds = pygame.sprite.Group()

    for i in range(cfg.WIDTH // cfg.TILE_SIZE):
        location = [i*cfg.TILE_SIZE, 600]
        img_path = cfg.LANDSCAPE_PATHS['grass1']
        ground = GroundClass(img_path, location)
        grounds.add(ground)
    grounds.draw(screen)


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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    print("a")
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print("d")

        updateFrame(screen)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
