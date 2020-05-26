import sys

import pygame

from interceptor.engine.hexgrid import HexGrid
from interceptor.fighter.pilot import Pilot
from interceptor.loader.dataload_damagetemplates import load_templates
from interceptor.loader.dataload_fighters import load_fighters
from interceptor.loader.dataload_weapons import load_weapons
from interceptor.states.states import States


class Movement(States):
    def __init__(self, **settings):
        States.__init__(self)
        self.__dict__.update(settings)

        # Text for the phase
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.text = self.font.render('Movement Phase', True, self.white, self.black)
        self.textRect = self.text.get_rect()
        # self.textRect.center = (50, 50)

        # TODO Trackers for what to update
        self.pilot_changed = False
        self.pilot_moved = False

        self.next = 'menu'

    def cleanup(self):
        print('cleaning up Game state stuff')

        # TODO Save information on what happened to the fighters?
        States.shared_data.update({'return_to': 'movement'})

    def startup(self):
        print('starting Game state stuff')
        self.hexgrid = States.shared_data.get('hexgrid')
        self.mission = States.shared_data.get('mission')
        # Mission info

        # TODO Get both lists of fighters from mission and randomize them.
        # Use that list for the turns, instead of pulling from mission.
        # Then, once all lists are exhausted, go back to interphase.

        self.current_pilot = self.mission.renegade_pilots[0]

        self.current_hex = (self.current_pilot.x, self.current_pilot.y)
        self.target_hex = None

        if self.current_hex is not None:
            self.current_hex_pointlist = self.hexgrid.generate_points_for_hex(self.current_hex[0], self.current_hex[1])
        else:
            self.current_hex_pointlist = None
        if self.target_hex is not None:
            self.target_hex_pointlist = self.hexgrid.generate_points_for_hex(self.target_hex[0], self.target_hex[1])
        else:
            self.target_hex_pointlist = None

        self.current_team = "RENEGADE"
        self.renegade_token = 0
        self.tog_token = -1

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
                    if self.tog_token >= len(self.mission.tog_pilots):
                        self.tog_token = 0
                    self.current_team = "TOG"
                    self.current_pilot = self.mission.tog_pilots[self.tog_token]
                elif self.current_team == "TOG":
                    self.renegade_token = self.renegade_token + 1
                    if self.renegade_token >= len(self.mission.renegade_pilots):
                        self.renegade_token = 0
                    self.current_team = "RENEGADE"
                    self.current_pilot = self.mission.renegade_pilots[self.renegade_token]
                self.pilot_changed = True
            elif event.key == pygame.K_RETURN:
                # TODO temporary - forces back to interphase just to test out game state swap
                self.next = 'interphase'
                self.done = True
            else:
                print(f'Game State Keydown ({event.key} was pressed, which is currently unbound.')

    def update(self, screen, dt):
        if self.pilot_changed or self.pilot_moved:
            print(f"Hex changed. Updating coordinates to {self.current_pilot.x}, {self.current_pilot.y}")
            self.current_hex = (self.current_pilot.x, self.current_pilot.y)
            self.current_hex_pointlist = self.hexgrid.generate_points_for_hex(self.current_hex[0], self.current_hex[1])
            # TODO Have a function that resets all change information
            self.pilot_changed = False
            self.pilot_moved = False

        self.draw(screen)

    def draw(self, screen):
        screen.fill(self.black)

        # Display background image
        screen.blit(self.space_bg, (0, 0))

        # TODO Move this to hexgrid?
        for hexpointlist in self.hexgrid.generate_points():
            pygame.draw.lines(screen, self.blue, self.closed, hexpointlist, self.thickness)  # redraw the points

        if self.current_hex_pointlist is not None:
            pygame.draw.lines(screen, self.green, self.closed, self.current_hex_pointlist, self.thickness)  # redraw the points

        for pilot in self.mission.renegade_pilots:
            pilot.draw(screen, self.hexgrid, .3)

        for pilot in self.mission.tog_pilots:
            pilot.draw(screen, self.hexgrid, .3)

        # Marker for the phase
        screen.blit(self.text, self.textRect)

        # update the screen
        pygame.display.update()
