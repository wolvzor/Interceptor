import unittest
import os

from interceptor.loader.dataload_weapons import load_weapons

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestDataLoaderWeapons(unittest.TestCase):
    def test_dataload_weapons_main(self):
        self.filename = os.path.join(THIS_DIR, '../../interceptor/data/weapon_data.csv')
        self.weapons = load_weapons(self.filename)
        self.assertTrue(len(self.weapons) > 0, "Number of weapons must be greater than zero")


if __name__ == '__main__':
    unittest.main()
