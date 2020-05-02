# TIL A weapon can't own a damage template.
# The damage template needs to be a look-up once the damage is calculated (from range and type of weapon)
# A damage template is a matrix and a midpoint. The midpoint is used to determine which armor column the damage should
# start being applied.


class DamageTemplate(object):

    def __init__(self, name="template_name", damage_type="laser", total_damage=0, width=1, mid=0, damage_list=[]):
        self.name = name
        self.damage_type = damage_type
        self.total_damage = int(total_damage)
        self.width = int(width)
        self.midpoint = int(mid)
        self.damage_list = damage_list

    def __str__(self):
        return f"{self.name} {self.damage_type} {self.total_damage} {self.width} {self.midpoint} {self.damage_list}"
