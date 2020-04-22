# TODO This is just a stub for now.
# TIL A weapon can't own a damage template.
# The damage template needs to be a look-up once the damage is calculated (from range and type of weapon)
# A damage template is a matrix and a midpoint. The midpoint is used to determine which armor column the damage should
# start being applied.


class DamageTemplate(object):

    def __init__(self, matrix=[], mid=0):
        self.damage_template = matrix
        self.midpoint = mid
