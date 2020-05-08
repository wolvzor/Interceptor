import unittest

from interceptor.fighter.fighter import Fighter
from interceptor.fighter.pilot import Pilot


class PilotTest(unittest.TestCase):
    def test_initialization_defaults(self):
        self.pilot = Pilot()
        self.assertEqual("John Doe", self.pilot.name, "Default name must equal")
        self.assertEqual("void", self.pilot.callsign, "Default callsign must equal")
        self.assertTrue(self.pilot.piloting_skill > 2, "Default piloting must be greater than two")
        self.assertTrue(self.pilot.piloting_skill < 7, "Default piloting must be less than seven")
        self.assertTrue(self.pilot.gunnery_skill > 1, "Default gunnery must be greater than one")
        self.assertTrue(self.pilot.gunnery_skill < 7, "Default gunnery must be less than seven")
        self.assertTrue(isinstance(self.pilot.fighter, Fighter), "Must have a default fighter")

    def test_initialization(self):
        self.fighter = Fighter("Test Fighter", "Light Fighter", 1, 2, 3, 4, 5, 6, True, True, None, None, None)
        self.pilot = Pilot("Jane", "Minerva", 7, 8, self.fighter)
        self.assertEqual("Jane", self.pilot.name, "Name must equal")
        self.assertEqual("Minerva", self.pilot.callsign, "Callsign must equal")
        self.assertEqual(7, self.pilot.piloting_skill, "Piloting skill must equal")
        self.assertEqual(8, self.pilot.gunnery_skill, "Gunnery Skill must equal")
        self.assertEqual(self.fighter, self.pilot.fighter, "Fighter must equal")

    def test_hex(self):
        self.fighter = Fighter("Test Fighter", "Light Fighter", 1, 2, 3, 4, 5, 6, True, True, None, None, None)
        self.pilot = Pilot("Jane", "Minerva", 7, 8, self.fighter)
        self.assertEqual(0, self.pilot.x, "Initial hex x should be 0")
        self.assertEqual(0, self.pilot.y, "Initial hex y should be 0")
        self.assertEqual(0, self.pilot.heading, "Initial hex heading should be 0")

        self.pilot.change_hex(1, 2)
        self.pilot.change_heading(3)
        self.assertEqual(1, self.pilot.x, "New hex x should be 1")
        self.assertEqual(2, self.pilot.y, "New hex y should be 2")
        self.assertEqual(3, self.pilot.heading, "New hex heading should be 3")


if __name__ == '__main__':
    unittest.main()
