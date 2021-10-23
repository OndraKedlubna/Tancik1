import os

FPS = 40

WIDTH = 900
HEIGHT = 650
TILE_SIZE = 50

SCREENSIZE = (WIDTH, HEIGHT)
COLOR_SKY = (133, 193, 233)

TANCIK_PATHS = {
    'tank': os.path.join(os.getcwd(), 'resources/images/tank.png'),
    'tankl': os.path.join(os.getcwd(), 'resources/images/tankl.png'),
    'tankr': os.path.join(os.getcwd(), 'resources/images/tankr.png'),
    'tanklt': os.path.join(os.getcwd(), 'resources/images/tanklt.png'),
    'tankrt': os.path.join(os.getcwd(), 'resources/images/tankrt.png')
}

LANDSCAPE_PATHS = {
    'grass1': os.path.join(os.getcwd(), 'resources/images/grass1.png')
}

ICON_PATHS = {
    'turbo': os.path.join(os.getcwd(), 'resources/images/turbo.png')
}

FONTPATH = os.path.join(os.getcwd(), 'resources/font/FZSTK.TTF')
