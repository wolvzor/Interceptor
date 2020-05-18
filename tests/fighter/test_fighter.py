import unittest

from interceptor.fighter.weapon import Weapon
from interceptor.fighter.fighter import Fighter, generate_shields, generate_armor
from interceptor.fighter.fighter_weapons import FighterWeapons


class FighterTest(unittest.TestCase):
    def test_initialization_defaults(self):
        self.fighter = Fighter()
        self.assertEqual("", self.fighter.name, "Fighter class must match")
        self.assertEqual("Light Fighter", self.fighter.fighter_class, "Fighter class must match")
        self.assertEqual(0, self.fighter.mass, "Mass must match")
        self.assertEqual(0, self.fighter.cost, "Cost must match")
        self.assertEqual(0, self.fighter.center_engine, "Center engine must match")
        self.assertEqual(0, self.fighter.right_engine, "Right engine must match")
        self.assertEqual(0, self.fighter.left_engine, "Left engine must match")
        self.assertEqual(0, self.fighter.thrust, "Thrust must match")
        self.assertEqual(False, self.fighter.streamlining, "Streamlining must match")
        self.assertEqual(False, self.fighter.antigrav, "Antigrav must match")
        self.assertEqual(None, self.fighter.shields, "Shields must match")
        self.assertEqual(None, self.fighter.armors, "Armor must match")
        self.assertEqual(None, self.fighter.weapons, "Weapons must match")

    def test_initialization(self):
        self.test_shields = generate_shields(50, 40, 40, 40)
        self.test_armors = generate_armor(100, 60, 60, 100)
        self.test_weapons = FighterWeapons()
        self.test_weapons.add_weapon("bow",
                                      Weapon("MDC 8", "MDC", dict([(1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8)])
                                             , 6, 24, 108000))
        self.fighter = Fighter("Avenger", "Heavy Fighter", 175, 3552300, 0, 1200, 1200, 7, True, False,
                               self.test_shields, self.test_armors, self.test_weapons)
        self.assertEqual("Avenger", self.fighter.name, "Fighter class must match")
        self.assertEqual("Heavy Fighter", self.fighter.fighter_class, "Fighter class must match")
        self.assertEqual(175, self.fighter.mass, "Mass must match")
        self.assertEqual(3552300, self.fighter.cost, "Cost must match")
        self.assertEqual(0, self.fighter.center_engine, "Center engine must match")
        self.assertEqual(1200, self.fighter.right_engine, "Right engine must match")
        self.assertEqual(1200, self.fighter.left_engine, "Left engine must match")
        self.assertEqual(7, self.fighter.thrust, "Thrust must match")
        self.assertEqual(True, self.fighter.streamlining, "Streamlining must match")
        self.assertEqual(False, self.fighter.antigrav, "Antigrav must match")
        self.assertEqual(self.test_shields, self.fighter.shields, "Shields must match")
        self.assertEqual(self.test_armors, self.fighter.armors, "Armor must match")
        self.assertEqual(self.test_weapons, self.fighter.weapons, "Weapons must match")

    def test_turning(self):
        self.test_shields = generate_shields(50, 40, 40, 40)
        self.test_armors = generate_armor(100, 60, 60, 100)
        self.test_weapons = FighterWeapons()
        self.test_weapons.add_weapon("bow",
                                      Weapon("MDC 8", "MDC", dict([(1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8)])
                                             , 6, 24, 108000))
        self.fighter = Fighter("Avenger", "Heavy Fighter", 175, 3552300, 0, 1200, 1200, 7, True, False,
                               self.test_shields, self.test_armors, self.test_weapons)

        self.assertEqual(0, self.fighter.heading, "Starting heading must be 0")

        self.fighter.turn_right()
        self.assertEqual(5, self.fighter.heading, "Heading must have turned right")

        self.fighter.turn_right()
        self.assertEqual(4, self.fighter.heading, "Heading must have turned right")

        self.fighter.turn_left()
        self.assertEqual(5, self.fighter.heading, "Heading must have turned left")

        self.fighter.turn_left()
        self.assertEqual(0, self.fighter.heading, "Heading must have turned left")

        self.fighter.turn_left()
        self.assertEqual(1, self.fighter.heading, "Heading must have turned left")

    def test_moving_forward(self):
        self.test_shields = generate_shields(50, 40, 40, 40)
        self.test_armors = generate_armor(100, 60, 60, 100)
        self.test_weapons = FighterWeapons()
        self.test_weapons.add_weapon("bow",
                                     Weapon("MDC 8", "MDC", dict([(1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8)])
                                            , 6, 24, 108000))
        self.fighter = Fighter("Avenger", "Heavy Fighter", 175, 3552300, 0, 1200, 1200, 7, True, False,
                               self.test_shields, self.test_armors, self.test_weapons)

        self.assertEqual(0, self.fighter.heading, "Starting heading must be 0")
        self.assertEqual(0, self.fighter.x, "Starting x position must be 0")
        self.assertEqual(0, self.fighter.y, "Starting y position must be 0")

        self.fighter.move_forward()
        self.assertEqual(1, self.fighter.x, "New x position must be 1")
        self.assertEqual(0, self.fighter.y, "New y position must be 0")

        self.fighter.move_forward()
        self.assertEqual(2, self.fighter.x, "New x position must be 2")
        self.assertEqual(0, self.fighter.y, "New y position must be 0")

        self.fighter.turn_right()
        self.fighter.move_forward()
        self.assertEqual(2, self.fighter.x, "New x position must be 2")
        self.assertEqual(1, self.fighter.y, "New y position must be 1")

        self.fighter.move_forward()
        self.assertEqual(3, self.fighter.x, "New x position must be 3")
        self.assertEqual(2, self.fighter.y, "New y position must be 2")

        self.fighter.turn_right()
        self.fighter.move_forward()
        self.assertEqual(2, self.fighter.x, "New x position must be 2")
        self.assertEqual(3, self.fighter.y, "New y position must be 3")

        self.fighter.move_forward()
        self.assertEqual(2, self.fighter.x, "New x position must be 2")
        self.assertEqual(4, self.fighter.y, "New y position must be 4")

        self.fighter.turn_right()
        self.fighter.move_forward()
        self.assertEqual(1, self.fighter.x, "New x position must be 1")
        self.assertEqual(4, self.fighter.y, "New y position must be 4")

        self.fighter.move_forward()
        self.assertEqual(0, self.fighter.x, "New x position must be 0")
        self.assertEqual(4, self.fighter.y, "New y position must be 4")

        self.fighter.turn_right()
        self.fighter.move_forward()
        self.assertEqual(-1, self.fighter.x, "New x position must be -1")
        self.assertEqual(3, self.fighter.y, "New y position must be 3")

        self.fighter.move_forward()
        self.assertEqual(-1, self.fighter.x, "New x position must be -1")
        self.assertEqual(2, self.fighter.y, "New y position must be 2")

        self.fighter.turn_right()
        self.fighter.move_forward()
        self.assertEqual(-1, self.fighter.x, "New x position must be -1")
        self.assertEqual(1, self.fighter.y, "New y position must be 1")

        self.fighter.move_forward()
        self.assertEqual(0, self.fighter.x, "New x position must be 0")
        self.assertEqual(0, self.fighter.y, "New y position must be 0")


if __name__ == '__main__':
    unittest.main()
