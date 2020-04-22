import unittest

from interceptor.fighter.damagetemplate import DamageTemplate


class DamageTemplateTest(unittest.TestCase):
    def test_init(self):
        self.damagetemplate = DamageTemplate()
        self.assertEqual([], self.damagetemplate.damage_template, "Template must have blank array")
        self.assertEqual(0, self.damagetemplate.midpoint, "Template must have 0 as default midpoint")

        self.damagetemplate2 = DamageTemplate([[1, 1, 1], [0, 1, 0]], 1)
        self.assertEqual([[1, 1, 1], [0, 1, 0]], self.damagetemplate2.damage_template, "Template must have matrix")
        self.assertEqual(1, self.damagetemplate2.midpoint, "Template must have the correct midpoint")


if __name__ == '__main__':
    unittest.main()
