import cfg


class UpgradesClass:

    def __init__(self):
        self.speed = 1
        self.speedImagePath = cfg.TANCIK_PATHS["tpod%d" % self.speed]
        pass

    def get_speed(self):
        return cfg.UPGRADES.get('speed').get(self.speed).get('value')

    def upgrade_speed(self):
        if self.speed < cfg.UPGRADES.get('speed').get('cap'):
            self.speed += 1
            self.speedImagePath = cfg.TANCIK_PATHS["tpod%d" % self.speed]
            return True
        return False
