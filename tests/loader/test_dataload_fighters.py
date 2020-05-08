import unittest
import os

from interceptor.fighter.armor import Armor
from interceptor.loader.dataload_fighters import load_fighters
from interceptor.loader.dataload_weapons import load_weapons

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestDataLoaderFighters(unittest.TestCase):
    def test_dataload_fighters_main(self):
        self.filename_weapons = os.path.join(THIS_DIR, '../../interceptor/data/weapon_data.csv')
        self.weapons = load_weapons(self.filename_weapons)

        self.filename = os.path.join(THIS_DIR, '../../interceptor/data/fighter_renegade_data.json')
        self.fighters = load_fighters(self.filename, self.weapons, "../../interceptor/")
        self.assertTrue(len(self.fighters) > 0, "Number of fighters must be greater than zero")

        self.fighter = self.fighters.get('Cheetah')
        self.assertEqual("Cheetah", self.fighter.name, "Name must match")
        self.assertEqual("Light Fighter", self.fighter.fighter_class, "Class must match")
        self.assertEqual(73, self.fighter.mass, "Mass must match")
        self.assertEqual(2366300, self.fighter.cost, "Cost must match")
        self.assertEqual(600, self.fighter.center_engine, "Center engine must match")
        self.assertEqual(450, self.fighter.right_engine, "Right engine must match")
        self.assertEqual(450, self.fighter.left_engine, "Left engine must match")
        self.assertEqual(10, self.fighter.thrust, "Thrust must match")
        self.assertEqual(True, self.fighter.streamlining, "Streamlining must match")
        self.assertEqual(False, self.fighter.antigrav, "Antigrav must match")

        self.assertEqual(50, self.fighter.shields.get('bow'), "shields must match")
        self.assertEqual(40, self.fighter.shields.get('right'), "shields must match")
        self.assertEqual(40, self.fighter.shields.get('left'), "shields must match")
        self.assertEqual(50, self.fighter.shields.get('stern'), "shields must match")

        self.assertEqual(vars(Armor(50)), vars(self.fighter.armors.get('bow')), "armor must match")
        self.assertEqual(vars(Armor(30)), vars(self.fighter.armors.get('right')), "armor must match")
        self.assertEqual(vars(Armor(30)), vars(self.fighter.armors.get('left')), "armor must match")
        self.assertEqual(vars(Armor(50)), vars(self.fighter.armors.get('stern')), "armor must match")

        self.assertEqual(1, self.fighter.weapons.bow.__len__(), "Weapon size must match for bow weapons")
        self.assertEqual(2, self.fighter.weapons.left.__len__(), "Weapon size must match for left weapons")
        self.assertEqual(2, self.fighter.weapons.right.__len__(), "Weapon size must match for right weapons")

        self.assertEqual("EPC 9", self.fighter.weapons.left[1].name, "Weapon name must match")


if __name__ == '__main__':
    unittest.main()
