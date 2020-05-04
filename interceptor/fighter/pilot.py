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

    # Returns a tuple of piloting skill and gunnery skill
    @staticmethod
    def generate_beginner_skill_level():
        roll = random.randint(1, 10)
        return Pilot.beginning_skill_table[roll]
