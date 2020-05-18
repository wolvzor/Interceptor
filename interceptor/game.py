import pygame

from pygame import *
from interceptor.states.control import Control
from interceptor.states.game import Game
from interceptor.states.menu import Menu

screen_height = 900
screen_width = 1600

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

settings = {
    'size': (screen_width, screen_height),
    'fps': 60
}

app = Control(**settings)
state_dict = {
    'menu': Menu(**settings),
    'game': Game(**settings)
}
app.setup_states(state_dict, 'menu')
app.main_game_loop()
pygame.quit()
sys.exit()