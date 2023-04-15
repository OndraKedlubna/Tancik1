import os

FPS = 60

WIDTH = 1000
HEIGHT = 650
TILE_SIZE = 50

SCREENSIZE = (WIDTH, HEIGHT)
COLOR_SKY = (133, 193, 233)

PARAM_TURBO_CHARGE = 200
PARAM_TURBO_FUEL = 60

MAX_LEVEL = 2

ENEMIES = {
    'eminion': {
        'speedx': 2,
        'speedy': 4,
        'reload': 20,
    },
    'eminion2': {
        'speedx': 4,
        'speedy': 4,
        'reload': 20,
    }
}

LEVELS = {
    1: {
        'eminion': 1,
        'eminion2': 1,
    },
    2: {
        'eminion2': 5,
    }
}

ENEMIES_LIMIT = {
    1: 1,
    2: 1
}

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
    'turbo': os.path.join(os.getcwd(), 'resources/images/turbo.png'),
    'ishoot': os.path.join(os.getcwd(), 'resources/images/ishoot.png')
}

SHOOT_PATHS = {
    'tshoot': os.path.join(os.getcwd(), 'resources/images/tshoot.png'),
    'teshoot': os.path.join(os.getcwd(), 'resources/images/teshoot.png')
}

ENEMIES_PATHS = {
    'eminion': os.path.join(os.getcwd(), 'resources/images/eminion.png'),
    'eminion2': os.path.join(os.getcwd(), 'resources/images/eminion2.png'),
    'eminionD': os.path.join(os.getcwd(), 'resources/images/eminionD.png'),
    'eminion2D': os.path.join(os.getcwd(), 'resources/images/eminionD.png')
}

FONTPATH = os.path.join(os.getcwd(), 'resources/font/FZSTK.TTF')
