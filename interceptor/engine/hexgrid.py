from math import sqrt


class HexGrid:

    def __init__(self, side=100, rows=1, columns=5, x_offset=0, y_offset=0):
        self.side = side
        self.rows = rows
        self.columns = columns
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.height = side * 2
        self.width = sqrt(3) * side

    def generate_points_for_hex(self, x, y):
        if y % 2 == 0:
            x_base = (x * self.width) + self.x_offset
            y_base = (y * self.height * 3/4) + self.y_offset
        else:
            x_base = (x * self.width) + self.width / 2 + self.x_offset
            y_base = (y * self.height * 3/4) + self.y_offset

        pointlist = [(x_base, y_base),
                     (x_base + self.width / 2, y_base - self.height / 4),
                     (x_base + self.width, y_base),
                     (x_base + self.width, y_base + self.height / 2),
                     (x_base + self.width / 2, y_base + (self.height * 3 / 4)),
                     (x_base, y_base + self.height / 2)]
        return pointlist

    def generate_points(self):
        hexes = []
        for r in range(self.rows):
            for c in range(self.columns):
                hexes.append(self.generate_points_for_hex(c, r))
        return hexes