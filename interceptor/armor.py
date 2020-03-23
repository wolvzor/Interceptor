# Armor
# Armor is represented by a 10x10 grid, with column and row.
# As damage takes away pieces of armor, there may be armor that is no longer attached to the base structure.
# This widowed armor, at the end of a combat round, detaches from the ship and can no longer be used for protection.

class Armor(object):
    armor = []

    def __init__(self):
        self.armor = self._construct()

    # generates full armor.
    # TODO generate armor based on rating (10-100)
    def _construct(self):
        self.armor = []
        for i in range(10):
            column_cells = []
            for j in range(10):
                column_cells.append(1)
            self.armor.append(column_cells)
        return self.armor

    def _damage_cell(self, row, column):
        self.armor[row][column] = 0
        return self.armor

    def _reconcile_widowed(self):
        return self.armor
