import unittest

from interceptor.fighter.damagetemplate import DamageTemplate


class DamageTemplateTest(unittest.TestCase):
    def test_init(self):
        self.damagetemplate = DamageTemplate()
        self.assertEqual("template_name", self.damagetemplate.name, "Template must have default name")
        self.assertEqual("laser", self.damagetemplate.damage_type, "Template must have default type")
        self.assertEqual(0, self.damagetemplate.total_damage, "Template must have 0 as default total damage")
        self.assertEqual(1, self.damagetemplate.width, "Template must have 1 as default width")
        self.assertEqual(0, self.damagetemplate.midpoint, "Template must have 0 as default midpoint")
        self.assertEqual([], self.damagetemplate.damage_list, "Template must have blank array")

        self.damage_list = [5, 3, 3, 1, 0, 0, 0, 0, 0, 0]
        self.damagetemplate2 = DamageTemplate("MDC 12", "MDC", "12", "5", "2", self.damage_list)
        self.assertEqual("MDC 12", self.damagetemplate2.name, "Template must have a name")
        self.assertEqual("MDC", self.damagetemplate2.damage_type, "Template must have a type")
        self.assertEqual(12, self.damagetemplate2.total_damage, "Template must have 12 as total damage")
        self.assertEqual(5, self.damagetemplate2.width, "Template must have 5 as width")
        self.assertEqual(2, self.damagetemplate2.midpoint, "Template must have 2 as midpoint")
        self.assertEqual(self.damage_list, self.damagetemplate2.damage_list, "Template must have damage list")


if __name__ == '__main__':
    unittest.main()
