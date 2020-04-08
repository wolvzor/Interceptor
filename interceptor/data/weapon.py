def fill_damage_ranges_if_missing(ranges):
    for key in Weapon.default_ranges:
        if ranges.get(key) is None:
            ranges.update({key: Weapon.default_ranges.get(key)})
    return ranges


class Weapon(object):
    default_ranges = dict(
        [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0),
         (14, 0), (15, 0)])

    def __init__(self, name="weapon_name", type="laser", ranges=None, power=0, tonnage=0, cost=0):
        if ranges is None:
            self.ranges = Weapon.default_ranges
        else:
            self.ranges = fill_damage_ranges_if_missing(ranges)
        self.name = name
        self.type = type
        self.power = power
        self.tonnage = tonnage
        self.cost = cost

    # Returns a tuple for damage type and damage amount. This is used to look up the correct damage template
    def _calculate_damage(self, range):
        self.damage = self.ranges.get(range)
        if self.damage is None:
            self.damage = 0
        return self.type, self.damage
