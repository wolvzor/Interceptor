import sys

import pygame

from interceptor.engine.hexgrid import HexGrid
from interceptor.engine.mission import Mission
from interceptor.fighter.pilot import Pilot
from interceptor.loader.dataload_damagetemplates import load_templates
from interceptor.loader.dataload_fighters import load_fighters
from interceptor.loader.dataload_weapons import load_weapons
from interceptor.states.states import States


class Interphase(States):
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

        self.mission = Mission(renegade_fighters, tog_fighters)

        self.hexgrid = HexGrid(60, 10, 10, 50, 50)
        self.hexes = self.hexgrid.generate_points()

        self.next = 'menu'

        # Text for the phase
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.text = self.font.render('Inter Phase', True, self.white, self.black)
        self.textRect = self.text.get_rect()
        # self.textRect.center = (50, 50)

    def cleanup(self):
        print('cleaning up Game state stuff')
        print('Saving information into shared data')
        States.shared_data.update({'hexgrid': self.hexgrid})
        States.shared_data.update({'mission': self.mission})
        States.shared_data.update({'return_to': 'interphase'})

    def startup(self):
        print('starting Game state stuff')

    def get_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.next = 'movement'
                self.done = True
            elif event.key == pygame.K_ESCAPE:
                self.next = 'menu'
                self.done = True
            else:
                print(f'Game State Keydown ({event.key} was pressed, which is currently unbound.')

    def update(self, screen, dt):
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

        for pilot in self.mission.renegade_pilots:
            pilot.draw(screen, self.hexgrid, .3)

        for pilot in self.mission.tog_pilots:
            pilot.draw(screen, self.hexgrid, .3)

        # Marker for the phase
        screen.blit(self.text, self.textRect)

        # update the screen
        pygame.display.update()
