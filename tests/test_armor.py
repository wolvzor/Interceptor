import unittest
from interceptor.armor import Armor

class ArmorTest(unittest.TestCase):
    def setUp(self):
        self.armor = Armor()

    def test_generate_armor(self):
        self.armor = Armor()
        self.assertEqual(1, self.armor.armor[0][0])
        self.assertEqual(1, self.armor.armor[0][9])
        self.assertEqual(1, self.armor.armor[9][0])
        self.assertEqual(1, self.armor.armor[9][9])

    def test_damage_cell(self):
        self.armor._damage_cell(0, 0)
        self.assertEqual(0, self.armor.armor[0][0])

    def test_reconcile_widowed(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
