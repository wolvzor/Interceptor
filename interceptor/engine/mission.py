from interceptor.fighter.pilot import Pilot

# TODO Change to be from a dataload as well, instead of hardcoding fighters
class Mission(object):
    def __init__(self, renegade_fighters, tog_fighters):
        # Define starting Pilots
        renegade_pilot = Pilot("Jane", "Minerva", 5, 4, renegade_fighters['Cheetah'])
        renegade_pilot.change_heading(0)
        renegade_pilot.change_hex(4, 3)

        renegade_pilot2 = Pilot("Jane", "Minerva", 5, 4, renegade_fighters['Guardian'])
        renegade_pilot2.change_heading(2)
        renegade_pilot2.change_hex(3, 2)

        tog_pilot = Pilot("John", "Invictus", 6, 6, tog_fighters['Lancea'])
        tog_pilot.change_heading(4)
        tog_pilot.change_hex(2, 2)

        tog_pilot2 = Pilot("John", "Invictus", 6, 6, tog_fighters['Verutum'])
        tog_pilot2.change_heading(3)
        tog_pilot2.change_hex(1, 0)
        self.renegade_pilots = [renegade_pilot, renegade_pilot2]
        self.tog_pilots = [tog_pilot, tog_pilot2]