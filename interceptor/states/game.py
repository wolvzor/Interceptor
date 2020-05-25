import sys

import pygame

from interceptor.engine.hexgrid import HexGrid
from interceptor.fighter.pilot import Pilot
from interceptor.loader.dataload_damagetemplates import load_templates
from interceptor.loader.dataload_fighters import load_fighters
from interceptor.loader.dataload_weapons import load_weapons
from interceptor.states.states import States


class Game(States):
    def __init__(self, **settings):
        States.__init__(self)
        self.__dict__.update(settings)

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
        # TODO Add a way to change the current pilot.
        self.current_pilot = self.renegade_pilots[0]

        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.closed = True
        self.black = (0, 0, 0)

        # TODO Encapsulate target and current hex somewhere
        self.current_hex = (self.current_pilot.x, self.current_pilot.y)
        self.target_hex = None

        # Drawing some lines
        self.thickness = 1

        self.hexgrid = HexGrid(60, 10, 10, 50, 50)
        self.hexes = self.hexgrid.generate_points()

        if self.current_hex is not None:
            self.current_hex_pointlist = self.hexgrid.generate_points_for_hex(self.current_hex[0], self.current_hex[1])
        else:
            self.current_hex_pointlist = None
        if self.target_hex is not None:
            self.target_hex_pointlist = self.hexgrid.generate_points_for_hex(self.target_hex[0], self.target_hex[1])
        else:
            self.target_hex_pointlist = None

        # TODO Remove troubleshooting information
        print(f"hexes information: {self.hexes}")
        print(f"hexes information: {self.current_hex_pointlist}")
        print(f"hexes information: {self.target_hex_pointlist}")

        # background space picture
        self.space_bg = pygame.image.load('data/space/potw1716a.jpg')
        self.space_bg = pygame.transform.scale(self.space_bg, self.size)

        self.next = 'menu'

        self.current_team = "RENEGADE"
        self.renegade_token = 0
        self.tog_token = -1

        # TODO Trackers for what to update
        self.pilot_changed = False
        self.pilot_moved = False

    def cleanup(self):
        print('cleaning up Game state stuff')

    def startup(self):
        print('starting Game state stuff')

    def get_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.current_pilot.turn_left()
                self.pilot_moved = True
            elif event.key == pygame.K_RIGHT:
                self.current_pilot.turn_right()
                self.pilot_moved = True
            elif event.key == pygame.K_UP:
                self.current_pilot.move_forward()
                self.pilot_moved = True
            elif event.key == pygame.K_ESCAPE:
                self.done = True
            elif event.key == pygame.K_SPACE:
                # TODO Extract this into a turn-keeping game state class.
                if self.current_team == "RENEGADE":
                    self.tog_token = self.tog_token + 1
                    if self.tog_token >= len(self.tog_pilots):
                        self.tog_token = 0
                    self.current_team = "TOG"
                    self.current_pilot = self.tog_pilots[self.tog_token]
                elif self.current_team == "TOG":
                    self.renegade_token = self.renegade_token + 1
                    if self.renegade_token >= len(self.renegade_pilots):
                        self.renegade_token = 0
                    self.current_team = "RENEGADE"
                    self.current_pilot = self.renegade_pilots[self.renegade_token]
                self.pilot_changed = True

            else:
                print(f'Game State Keydown ({event.key} was pressed, which is currently unbound.')

    def update(self, screen, dt):


        # TODO Change current hex if necessary
        if self.pilot_changed or self.pilot_moved:
            print(f"Hex changed. Updating coordinates to {self.current_pilot.x}, {self.current_pilot.y}")
            self.current_hex = (self.current_pilot.x, self.current_pilot.y)
            self.current_hex_pointlist = self.hexgrid.generate_points_for_hex(self.current_hex[0], self.current_hex[1])
            # TODO Have a function that resets all change information
            self.pilot_changed = False
            self.pilot_moved = False

        # TODO Change target hex if necessary

        self.draw(screen)

    def draw(self, screen):
        # erase the screen
        screen.fill(self.black)

        # Display background image
        screen.blit(self.space_bg, (0, 0))

        # draw the updated picture
        # TODO Move this to hexgrid?
        for hexpointlist in self.hexes:
            pygame.draw.lines(screen, self.blue, self.closed, hexpointlist, self.thickness)  # redraw the points

        if self.current_hex_pointlist is not None:
            pygame.draw.lines(screen, self.green, self.closed, self.current_hex_pointlist, self.thickness)  # redraw the points

        if self.target_hex_pointlist is not None:
            pygame.draw.lines(screen, self.red, self.closed, self.target_hex_pointlist, self.thickness)  # redraw the points

        for pilot in self.renegade_pilots:
            pilot.draw(screen, self.hexgrid, .3)

        for pilot in self.tog_pilots:
            pilot.draw(screen, self.hexgrid, .3)

        # update the screen
        pygame.display.update()
