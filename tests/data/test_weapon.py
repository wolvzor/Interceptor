import unittest
from interceptor.data.weapon import Weapon


class WeaponTest(unittest.TestCase):
    def test_defaults(self):
        self.weapon = Weapon()
        self.assertEqual(0, self.weapon.cost, "Cost must be zero")
        self.assertEqual("weapon_name", self.weapon.name, "Weapon name must be default")
        self.assertEqual("laser", self.weapon.type, "Weapon type must be default")
        self.assertEqual(0, self.weapon.power, "Power must be zero")
        self.assertEqual(0, self.weapon.tonnage, "Tonnage must be zero")
        print(self.weapon.ranges)
        for i in range(1, 15):
            self.assertEqual(0, self.weapon.ranges.get(i), f"Range for {i} must be zero")

    def test_arguments(self):
        self.weapon = Weapon("MDC 8", "MDC", dict([(1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8)]), 6, 24, 108000)
        self.assertEqual(108000, self.weapon.cost, "Cost must match argument")
        self.assertEqual("MDC 8", self.weapon.name, "Weapon name must match argument")
        self.assertEqual("MDC", self.weapon.type, "Weapon type must match argument")
        self.assertEqual(6, self.weapon.power, "Power must match argument")
        self.assertEqual(24, self.weapon.tonnage, "Tonnage must match argument")
        print(self.weapon.ranges)
        for i in range(1, 6):
            self.assertEqual(8, self.weapon.ranges.get(i), f"Range for {i} must be 8")
        for i in range(7, 15):
            self.assertEqual(0, self.weapon.ranges.get(i), f"Range for {i} must be 0")

    def test_calculate_damage(self):
        self.weapon = Weapon("NPC 9", "NPC", dict([(1, 1), (2, 6), (3, 6), (4, 9), (5, 9), (6, 9)]), 7, 16, 104000)
        self.assertEqual(("NPC", 1), self.weapon._calculate_damage(1), "Damage at range 1 must be 1 NPC")
        self.assertEqual(("NPC", 6), self.weapon._calculate_damage(2), "Damage at range 2 must be 6 NPC")
        self.assertEqual(("NPC", 6), self.weapon._calculate_damage(3), "Damage at range 3 must be 6 NPC")
        self.assertEqual(("NPC", 9), self.weapon._calculate_damage(4), "Damage at range 4 must be 9 NPC")
        self.assertEqual(("NPC", 9), self.weapon._calculate_damage(5), "Damage at range 5 must be 9 NPC")
        self.assertEqual(("NPC", 9), self.weapon._calculate_damage(6), "Damage at range 6 must be 9 NPC")
        self.assertEqual(("NPC", 0), self.weapon._calculate_damage(7), "Damage at range 7 must be 0 NPC")
        self.assertEqual(("NPC", 0), self.weapon._calculate_damage(57), "Damage at range 47 must be 0 NPC")

if __name__ == '__main__':
    unittest.main()
