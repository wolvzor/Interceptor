import unittest

from interceptor.fighter.weapon import Weapon
from interceptor.fighter.fighter_weapons import FighterWeapons


class FighterWeaponsTest(unittest.TestCase):
    def test_add_weapons(self):
        self.fighter_weapons = FighterWeapons()
        self.bow_weapon = Weapon("MDC 8", "MDC", dict([(1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8)]), 6, 24, 108000)
        self.left_weapon = Weapon("NPC 9", "NPC", dict([(1, 1), (2, 6), (3, 6), (4, 9), (5, 9), (6, 9)]), 7, 16, 104000)
        self.right_weapon = Weapon("EPC 9", "EPC", dict([(1, 9), (2, 5), (3, 5), (4, 3), (5, 3), (6, 3)]),
                                   25, 6, 125000)
        self.one_weapon = Weapon("1.5/6", "LASER", dict([(1, 7), (2, 6), (3, 6)]), 10, 10, 120000)
        self.two_weapon = Weapon("1.5/3", "LASER", dict([(1, 4), (2, 3), (3, 3)]), 5, 5, 60000)
        self.fighter_weapons._add_weapon("bow", self.bow_weapon)
        self.fighter_weapons._add_weapon("left", self.left_weapon)
        self.fighter_weapons._add_weapon("right", self.right_weapon)
        self.fighter_weapons._add_weapon("one", self.one_weapon)
        self.fighter_weapons._add_weapon("two", self.two_weapon)
        self.assertEquals(1, self.fighter_weapons.bow.__len__(), "Bow weapon size must match")
        self.assertEquals(1, self.fighter_weapons.left.__len__(), "Left weapon size must match")
        self.assertEquals(1, self.fighter_weapons.right.__len__(), "Right weapon size must match")
        self.assertEquals(1, self.fighter_weapons.one.__len__(), "Turret one weapon size must match")
        self.assertEquals(1, self.fighter_weapons.two.__len__(), "Turret two weapon size must match")
        self.assertTrue(self.fighter_weapons.bow.__contains__(self.bow_weapon), "Bow weapons must include MDC 8")
        self.assertTrue(self.fighter_weapons.left.__contains__(self.left_weapon), "Left weapons must include NPC 9")
        self.assertTrue(self.fighter_weapons.right.__contains__(self.right_weapon), "Right weapons must include EPC 9")
        self.assertTrue(self.fighter_weapons.one.__contains__(self.one_weapon),
                        "Turret one weapons must include LASER 1.5/6")
        self.assertTrue(self.fighter_weapons.two.__contains__(self.two_weapon),
                        "Turret two weapons must include LASER 1.5/3")


if __name__ == '__main__':
    unittest.main()
