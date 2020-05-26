import sys

import pygame

from interceptor.states.states import States


class Menu(States):
    def __init__(self, **settings):
        States.__init__(self)
        self.__dict__.update(settings)
        self.next = 'interphase'

        # background title picture
        self.title_bg = pygame.image.load('data/menu/title.jpg')
        self.title_bg = pygame.transform.scale(self.title_bg, self.size)

    def cleanup(self):
        print('cleaning up Menu state stuff')

    def startup(self):
        print('starting Menu state stuff')
        if States.shared_data.get('return_to') is not None:
            self.next = States.shared_data.get('return_to')

    def get_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_RETURN:
                self.done = True
            else:
                print(f'Game State Keydown ({event.key} was pressed, which is currently unbound.')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.done = True

    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        # Display background image
        screen.blit(self.title_bg, (0, 0))
