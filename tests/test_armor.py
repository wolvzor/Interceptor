import copy
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

    def test_generate_armor_90(self):
        self.armor = Armor(90)
        self.expected_armor = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.assertListEqual(self.expected_armor, self.armor.armor)

    def test_generate_armor_110_exception(self):
        with self.assertRaises(ValueError) as context:
            Armor(110)

    def test_generate_armor_0_exception(self):
        with self.assertRaises(ValueError) as context:
            Armor(0)

    def test_damage_cell(self):
        self.armor._damage_cell(0, 0)
        self.assertEqual(0, self.armor.armor[0][0])

    def test_reconcile_widowed_uninjured(self):
        self.armor = Armor()
        self.old_armor = copy.deepcopy(self.armor)
        self.armor._reconcile_widowed()
        self.assertListEqual(self.old_armor.armor, self.armor.armor)

    def test_reconcile_widowed_positive_one(self):
        self.armor = Armor()
        self.armor._construct_from_matrix([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                           [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                                           [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                                           [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                                           [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                                           [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                                           [1, 1, 0, 1, 1, 1, 1, 1, 1, 1]])
        self.expected_armor = Armor()
        self.expected_armor._construct_from_matrix([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                                    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                                                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                                                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                                                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                                                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                                                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]])
        self.armor._reconcile_widowed()
        self.maxDiff = None
        self.assertListEqual(self.expected_armor.armor, self.armor.armor)

    def test_reconcile_widowed_positive_two(self):
        self.armor = Armor()
        self.armor._construct_from_matrix([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                           [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                                           [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
                                           [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                                           [1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
                                           [1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
                                           [1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
                                           [1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
                                           [1, 0, 1, 1, 0, 0, 1, 1, 1, 1]])
        self.expected_armor = Armor()
        self.expected_armor._construct_from_matrix([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                                    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                                                    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
                                                    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                                                    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                                                    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                                                    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                                                    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                                                    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1]])
        self.armor._reconcile_widowed()
        self.maxDiff = None
        self.assertListEqual(self.expected_armor.armor, self.armor.armor)

    def test_reconcile_widowed_positive_three(self):
        self.armor = Armor()
        self.armor._construct_from_matrix([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                           [1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
                                           [1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
                                           [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                                           [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                                           [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                                           [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                                           [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                                           [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                                           [1, 1, 1, 0, 1, 1, 0, 1, 1, 1]])
        self.expected_armor = Armor()
        self.expected_armor._construct_from_matrix([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                                    [1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
                                                    [1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
                                                    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                                                    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                                                    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                                                    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                                                    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                                                    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                                                    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]])
        self.armor._reconcile_widowed()
        self.maxDiff = None
        self.assertListEqual(self.expected_armor.armor, self.armor.armor)

    def test_reconcile_widowed_same(self):
        self.armor = Armor()
        self.armor._construct_from_matrix([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                           [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                                           [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
                                           [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                                           [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                           [1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
                                           [1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
                                           [1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
                                           [1, 0, 1, 1, 0, 0, 1, 1, 1, 1]])
        self.expected_armor = Armor()
        self.expected_armor._construct_from_matrix([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                                    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                                                    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
                                                    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                                                    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                                    [1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
                                                    [1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
                                                    [1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
                                                    [1, 0, 1, 1, 0, 0, 1, 1, 1, 1]])
        self.armor._reconcile_widowed()
        self.maxDiff = None
        self.assertListEqual(self.expected_armor.armor, self.armor.armor)


if __name__ == '__main__':
    unittest.main()
