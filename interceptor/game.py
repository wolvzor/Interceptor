from random import randrange

import pygame
import sys

from interceptor.engine.hexgrid import HexGrid
from interceptor.fighter.pilot import Pilot
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

# Define starting Pilots
renegade_pilot = Pilot("Jane", "Minerva", 5, 4, renegade_fighters['Cheetah'])
renegade_pilot.change_heading(0)
renegade_pilot.change_hex(4,3)

renegade_pilot2 = Pilot("Jane", "Minerva", 5, 4, renegade_fighters['Guardian'])
renegade_pilot2.change_heading(2)
renegade_pilot2.change_hex(3,2)
renegade_pilots = [renegade_pilot, renegade_pilot2]

tog_pilot = Pilot("John", "Invictus", 6, 6, tog_fighters['Lancea'])
tog_pilot.change_heading(4)
tog_pilot.change_hex(2,2)

tog_pilot2 = Pilot("John", "Invictus", 6, 6, tog_fighters['Verutum'])
tog_pilot2.change_heading(3)
tog_pilot2.change_hex(1,0)
tog_pilots = [tog_pilot, tog_pilot2]

# background space picture
space_bg = pygame.image.load('data/space/potw1716a.jpg')
space_bg = pygame.transform.scale(space_bg, (screen_width, screen_height))

while True:

    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # erase the screen
    screen.fill(black)

    # Display background image
    screen.blit(space_bg, (0, 0))

    # draw the updated picture
    for hexpointlist in hexes:
        pygame.draw.lines(screen, green, closed, hexpointlist, thickness)  # redraw the points

    for pilot in renegade_pilots:
        pilot.draw(screen, hexgrid, .3)

    for pilot in tog_pilots:
        pilot.draw(screen, hexgrid, .3)

    # update the screen
    pygame.display.update()
