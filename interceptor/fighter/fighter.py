import pygame

from interceptor.fighter.armor import Armor


def generate_shields(bow_rating, right_rating, left_rating, stern_rating):
    return dict([("bow", bow_rating), ("right", right_rating), ("left", left_rating), ("stern", stern_rating)])


def generate_armor(bow_rating, right_rating, left_rating, stern_rating):
    return dict([("bow", Armor(bow_rating)), ("right", Armor(right_rating)), ("left", Armor(left_rating)),
                 ("stern", Armor(stern_rating))])


class Fighter(object):

    def __init__(self, name="", fighter_class="Light Fighter", mass=0, cost=0, center_engine=0, right_engine=0,
                 left_engine=0,
                 thrust=0, streamlining=False, antigrav=False, shields=None, armors=None, weapons=None, image=None):
        # TODO Find out enumerations in Python
        self.name = name
        self.fighter_class = fighter_class
        self.mass = mass
        self.cost = cost
        self.center_engine = center_engine
        self.right_engine = right_engine
        self.left_engine = left_engine
        self.thrust = thrust
        self.streamlining = streamlining
        self.antigrav = antigrav
        self.shields = shields
        self.armors = armors
        self.weapons = weapons
        if image is None:
            self.image = None
        else:
            self.image = pygame.image.load(image)

        self.x = 0
        self.y = 0
        self.heading = 0
        self.current_thrust = self.thrust

    def change_hex(self, x, y):
        self.x = x
        self.y = y

    def change_heading(self, heading):
        self.heading = heading

    def turn_left(self):
        if self.heading < 5:
            self.heading = self.heading + 1
        else:
            self.heading = 0
        print(f"Heading of {self.name} changed to {self.heading}")

    def turn_right(self):
        if self.heading > 0:
            self.heading = self.heading - 1
        else:
            self.heading = 5
        print(f"Heading of {self.name} changed to {self.heading}")

    def change_thrust(self, thrust):
        self.current_thrust = thrust

    # TODO Extract this into a base drawable object
    def draw(self, screen, hexgrid, scale):
        rot = self.heading * 60
        (base_x, base_y) = hexgrid.calculate_object_drawing_tuple(self.x, self.y)
        # TODO Fix the -90 by changing the base image file.
        temp_image = pygame.transform.rotozoom(self.image, -90 + rot, scale)
        screen.blit(temp_image, (base_x, base_y))
