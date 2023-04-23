import cfg


class UpgradesClass:

    def __init__(self):
        self.speed = 1
        self.speedImagePath = cfg.TANCIK_PATHS["tpod%d" % self.speed]
        self.reload = 1
        self.reloadImagePath = cfg.TANCIK_PATHS["tcan%d" % self.speed]
        pass

    def get_speed(self):
        return cfg.UPGRADES.get('speed').get(self.speed).get('value')

    def upgrade_speed(self):
        if self.speed < cfg.UPGRADES.get('speed').get('cap'):
            self.speed += 1
            self.speedImagePath = cfg.TANCIK_PATHS["tpod%d" % self.speed]
            return True
        return False

    def get_reload(self):
        return cfg.UPGRADES.get('reload').get(self.reload).get('value')

    def upgrade_reload(self):
        if self.reload < cfg.UPGRADES.get('reload').get('cap'):
            self.reload += 1
            self.reloadImagePath = cfg.TANCIK_PATHS["tcan%d" % self.reload]
            return True
        return False
