import cfg


class UpgradesClass:

    def __init__(self):
        self.speed = 1
        pass

    def get_speed(self):
        return cfg.UPGRADES.get('speed').get(self.speed).get('value')

    def upgrade_speed(self):
        if self.speed < cfg.UPGRADES.get('speed').get('cap'):
            self.speed += 1
            return True
        return False
