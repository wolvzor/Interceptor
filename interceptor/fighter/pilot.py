import random

from interceptor.fighter.fighter import Fighter


class Pilot(object):
    beginning_skill_table = dict([(1, (6, 6)), (2, (5, 5)), (3, (5, 4)), (4, (5, 4)), (5, (5, 4)), (6, (5, 4)),
                                  (7, (5, 4)), (8, (5, 4)), (9, (4, 3)), (10, (3, 2))])

    def __init__(self, name="John Doe", callsign="void", piloting_skill=0, gunnery_skill=0, fighter=None):
        self.name = name
        self.callsign = callsign
        if piloting_skill == 0 and gunnery_skill == 0:
            self.piloting_skill, self.gunnery_skill = self.generate_beginner_skill_level()
        else:
            self.piloting_skill = piloting_skill
            self.gunnery_skill = gunnery_skill
        if fighter is None:
            self.fighter = Fighter()
        else:
            self.fighter = fighter

        self.x = 0
        self.y = 0
        self.current_thrust = self.fighter.thrust

    # TODO for alpha, pilots and fighers are always in the same hex.
    def change_hex(self, x, y):
        self.x = x
        self.y = y
        self.fighter.change_hex(x, y)

    def change_heading(self, heading):
        self.fighter.change_heading(heading)

    def turn_left(self):
        self.fighter.turn_left()

    def turn_right(self):
        self.fighter.turn_right()

    def move_forward(self):
        self.fighter.move_forward()

    # Returns a tuple of piloting skill and gunnery skill
    @staticmethod
    def generate_beginner_skill_level():
        roll = random.randint(1, 10)
        return Pilot.beginning_skill_table[roll]

    def draw(self, screen, hexgrid, scale):
        self.fighter.draw(screen, hexgrid, scale)
