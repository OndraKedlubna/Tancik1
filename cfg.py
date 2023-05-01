import os

FPS = 80

WIDTH = 1000
HEIGHT = 650
TILE_SIZE = 50

SCREENSIZE = (WIDTH, HEIGHT)
COLOR_SKY = (133, 193, 233)

PARAM_TURBO_CHARGE = 200
PARAM_TURBO_FUEL = 60

MAX_LEVEL = 4

ENEMIES = {
    'eminion': {
        'speedx': 2,
        'speedy': 4,
        'reload': 30,
        'score': 25,
        'shootspeed': 3
    },
    'eminion2': {
        'speedx': 4,
        'speedy': 4,
        'reload': 30,
        'score': 50,
        'shootspeed': 6
    },
    'eminion3': {
        'speedx': 2,
        'speedy': 4,
        'reload': 0,
        'score': 50,
        'shootspeed': 5
    },
    'eplane': {
        'speedx': 3,
        'speedy': 4,
        'reload': 30,
        'score': 25,
        'shootspeed': 3
    },
    'eplane2': {
        'speedx': 5,
        'speedy': 4,
        'reload': 30,
        'score': 50,
        'shootspeed': 6
    },
    'eplane3': {
        'speedx': 4,
        'speedy': 4,
        'reload': 0,
        'score': 50,
        'shootspeed': 4
    }
}

LEVELS = {
    1: {
        'eplane': 10,
        'eminion': 10,
        'eminion2': 1,
        'eminion3': 1,

    },
    2: {
        'eplane': 10,
        'eplane2': 5,
        'eplane3': 5,
        'eminion': 15,
        'eminion2': 8,
        'eminion3': 7,
    },
    3: {
        'eplane': 5,
        'eplane2': 10,
        'eplane3': 5,
        'eminion': 8,
        'eminion2': 15,
        'eminion3': 7,
    },
    4: {
        'eplane': 5,
        'eplane2': 10,
        'eplane3': 10,
        'eminion': 5,
        'eminion2': 15,
        'eminion3': 15,
    }

}

ENEMIES_LIMIT = {
    1: 1,
    2: 2,
    3: 2,
    4: 3
}

UPGRADES = {
    'speed': {
        1: {
            'value': 2,
            'cost': 1000,
            'image': 'tpod1'
        },
        2: {
            'value': 3,
            'cost': 2000,
            'image': 'tpod2'
        },
        3: {
            'value': 4,
            'cost': 4000,
            'image': 'tpod3'
        },
        4: {
            'value': 5,
            'cost': 0,
            'image': 'tpod4'
        },
        'cap': 4
    },
    'reload': {
        1: {
            'value': 120,
            'cost': 500,
            'image': 'tcan1'
        },
        2: {
            'value': 80,
            'cost': 1000,
            'image': 'tcan2'
        },
        3: {
            'value': 40,
            'cost': 1500,
            'image': 'tcan3'
        },
        4: {
            'value': 20,
            'cost': 0,
            'image': 'tcan4'
        },
        'cap': 4
    },
    'power': {
        1: {
            'value': 4,
            'cost': 1000,
            'image': 'tstrel1'
        },
        2: {
            'value': 6,
            'cost': 2000,
            'image': 'tstrel2'
        },
        3: {
            'value': 9,
            'cost': 4000,
            'image': 'tstrel3'
        },
        4: {
            'value': 14,
            'cost': 0,
            'image': 'tstrel4'
        },
        'cap': 4
    }
}

TANCIK_PATHS = {
    'tank': os.path.join(os.getcwd(), 'resources/images/tank.png'),
    'tankl': os.path.join(os.getcwd(), 'resources/images/tankl.png'),
    'tankr': os.path.join(os.getcwd(), 'resources/images/tankr.png'),
    'tanklt': os.path.join(os.getcwd(), 'resources/images/tanklt.png'),
    'tankrt': os.path.join(os.getcwd(), 'resources/images/tankrt.png'),
    'tpod1': os.path.join(os.getcwd(), 'resources/images/tpod1.png'),
    'tpod2': os.path.join(os.getcwd(), 'resources/images/tpod2.png'),
    'tpod3': os.path.join(os.getcwd(), 'resources/images/tpod3.png'),
    'tpod4': os.path.join(os.getcwd(), 'resources/images/tpod4.png'),
    'tcan1': os.path.join(os.getcwd(), 'resources/images/tcan1.png'),
    'tcan2': os.path.join(os.getcwd(), 'resources/images/tcan2.png'),
    'tcan3': os.path.join(os.getcwd(), 'resources/images/tcan3.png'),
    'tcan4': os.path.join(os.getcwd(), 'resources/images/tcan4.png'),
    'tstrel1': os.path.join(os.getcwd(), 'resources/images/tstrel1.png'),
    'tstrel2': os.path.join(os.getcwd(), 'resources/images/tstrel2.png'),
    'tstrel3': os.path.join(os.getcwd(), 'resources/images/tstrel3.png'),
    'tstrel4': os.path.join(os.getcwd(), 'resources/images/tstrel4.png')
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
    'eminion3': os.path.join(os.getcwd(), 'resources/images/eminion3.png'),
    'eminionD': os.path.join(os.getcwd(), 'resources/images/eminionD.png'),
    'eminion2D': os.path.join(os.getcwd(), 'resources/images/eminionD.png'),
    'eminion3D': os.path.join(os.getcwd(), 'resources/images/eminionD.png'),
    'eplane': os.path.join(os.getcwd(), 'resources/images/eplane.png'),
    'eplane2': os.path.join(os.getcwd(), 'resources/images/eplane2.png'),
    'eplane3': os.path.join(os.getcwd(), 'resources/images/eplane3.png'),
    'eplaneD': os.path.join(os.getcwd(), 'resources/images/eminionD.png'),
    'eplane2D': os.path.join(os.getcwd(), 'resources/images/eminionD.png'),
    'eplane3D': os.path.join(os.getcwd(), 'resources/images/eminionD.png')
}

FONTPATH = os.path.join(os.getcwd(), 'resources/font/FZSTK.TTF')
