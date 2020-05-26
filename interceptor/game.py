import pygame

from pygame import *
from interceptor.states.control import Control
from interceptor.states.game.interphase import Interphase
from interceptor.states.game.movement import Movement
from interceptor.states.menu import Menu

screen_height = 900
screen_width = 1600

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

# Dataloads

size = (screen_width, screen_height)

space_bg = pygame.image.load('data/space/potw1716a.jpg')
space_bg = pygame.transform.scale(space_bg, size)

settings = {
    'size': size,
    'fps': 60,
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'red': (255, 0, 0),
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'closed': True,
    'thickness': 1,
    'space_bg': space_bg
}

app = Control(**settings)
state_dict = {
    'menu': Menu(**settings),
    'interphase': Interphase(**settings),
    'movement': Movement(**settings)
}
app.setup_states(state_dict, 'menu')
app.main_game_loop()
pygame.quit()
sys.exit()