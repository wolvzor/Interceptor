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

    def _construct_from_matrix(self, matrix):
        self.armor = matrix

    def _damage_cell(self, row, column):
        self.armor[row][column] = 0
        return self.armor

    def _reconcile_widowed(self):
        widowed_armor = []
        column_cells = self.armor[0]
        widowed_armor.append(column_cells)
        for i in range(1, 10):
            column_cells = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            # First we check along the row...
            for j in range(10):
                column_cells[j] = self._attached_cell(i, j, column_cells, widowed_armor)
            # And then we reverse. This catches all possible connections, since we can't connect above.
            for j in reversed(range(10)):
                column_cells[j] = self._attached_cell(i, j, column_cells, widowed_armor)
            widowed_armor.append(column_cells)
        self.armor = widowed_armor
        return self.armor

    def _attached_cell(self, row, column, column_cells, widowed):
        if self.armor[row][column] == 0:
            return 0
        attached_value = widowed[row - 1][column]
        if column != 0:
            attached_value += column_cells[column - 1]
        if column != 9:
            attached_value += column_cells[column + 1]
        if attached_value > 1:
            attached_value = 1
        return attached_value