from random import randrange

import pygame
import sys

from interceptor.engine.hexgrid import HexGrid
from interceptor.loader.dataload_damagetemplates import load_templates
from interceptor.loader.dataload_fighters import load_fighters
from interceptor.loader.dataload_weapons import load_weapons

# Dataloads
weapon_list = load_weapons()
print(weapon_list)
for weapon in weapon_list:
    print(weapon)

damage_templates = load_templates()
print(damage_templates)
for key in damage_templates:
    print(damage_templates[key])

renegade_fighters = load_fighters('data/fighter_renegade_data.json', weapon_list)
print(renegade_fighters)
for key in renegade_fighters:
    print(renegade_fighters[key])

tog_fighters = load_fighters('data/fighter_tog_data.json', weapon_list)
print(tog_fighters)
for key in tog_fighters:
    print(tog_fighters[key])

# Pygame code - may move later

screen_height = 480
screen_width = 640

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

# Drawing some lines
black = (0, 0, 0)
green = (0, 255, 0)
closed = True
pointlist = [(100, 100), (186, 50), (273, 100), (273, 200), (186, 250), (100, 200)]
thickness = 1

hexgrid = HexGrid(60, 10, 10, 50, 50)
pointlist = hexgrid.generate_points_for_hex(0, 0)
hexes = hexgrid.generate_points()

# TODO Fit into pilot/fighter objects
cheetah = pygame.image.load('data/fighter/cheetah.gif')
cheetah = pygame.transform.rotozoom(cheetah, -90, .3)

while True:

    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # erase the screen
    screen.fill(black)

    # draw the updated picture

    # TODO updatePoints(points)  # changes the location of the points
    for hexpointlist in hexes:
        pygame.draw.lines(screen, green, closed, hexpointlist, thickness)  # redraw the points

    # TODO Right now it randomly draws on screen, which is fine since I just want to demonstrate that the drawing code
    # works at the fighter level. Later on we'll have fighter locations.
    for fighter in renegade_fighters:
        renegade_fighters[fighter].draw(screen, randrange(screen_width), randrange(screen_height), randrange(360), .3)

    for fighter in tog_fighters:
        tog_fighters[fighter].draw(screen, randrange(screen_width), randrange(screen_height), randrange(360), .3)

    # update the screen
    pygame.display.update()
