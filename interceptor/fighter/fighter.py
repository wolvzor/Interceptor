import os
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

    def draw(self, screen, x, y, rot, scale):
        # TODO Fix the -90 by changing the base image file.
        temp_image = pygame.transform.rotozoom(self.image, -90 + rot, scale)
        screen.blit(temp_image, (x, y))
