# TODO This is only for basic fighters. We are not doing cruisers yet.
class FighterWeapons(object):

    def __init__(self):
        self.bow = []
        self.left = []
        self.right = []

    def add_weapon(self, location, weapon):
        self.__dict__[location].append(weapon)
