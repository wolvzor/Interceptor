import unittest
import os

from interceptor.loader.dataload_damagetemplates import load_templates

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

class TestDataLoaderDamageTemplates(unittest.TestCase):
    def test_dataload_damage_main(self):
        self.filename = os.path.join(THIS_DIR, '../../interceptor/data/damage_template_data.csv')
        self.templates = load_templates(self.filename)
        self.assertTrue(len(self.templates) > 0, "Number of templates must be greater than zero")

        self.template = self.templates.get("MDC 12")
        self.assertEqual("MDC 12", self.template.name, "Name must be equal")
        self.assertEqual("MDC", self.template.damage_type, "Type must be equal")
        self.assertEqual(12, self.template.total_damage, "Total Damage must be equal")
        self.assertEqual(5, self.template.width, "Width must be equal")
        self.assertEqual(2, self.template.midpoint, "Midpoint must be equal")

        self.damage_list = self.template.damage_list
        self.assertEqual(5, self.damage_list[0], "Damage at row 0 must be 5")
        self.assertEqual(3, self.damage_list[1], "Damage at row 1 must be 3")
        self.assertEqual(3, self.damage_list[2], "Damage at row 2 must be 3")
        self.assertEqual(1, self.damage_list[3], "Damage at row 3 must be 1")
        self.assertEqual(0, self.damage_list[4], "Damage at row 4 must be 0")

if __name__ == '__main__':
    unittest.main()
