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

pygame.init()
screen = pygame.display.set_mode((640, 480))

# Drawing some lines
black = (0, 0, 0)
green = (0, 255, 0)
closed = True
pointlist = [(100, 100), (186, 50), (273, 100), (273, 200), (186, 250), (100, 200)]
thickness = 1

hexgrid = HexGrid(25, 10, 10, 50, 50)
pointlist = hexgrid.generate_points_for_hex(0, 0)
hexes = hexgrid.generate_points()

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

    # update the screen
    pygame.display.update()
