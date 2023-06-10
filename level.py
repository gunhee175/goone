import pygame
from settings import *
from random import choice, randint

class Level:
    def __init__(self, render):
        self.render = render
        self.game_paused = False

        # user interface
        self.menu_state = 'none'

    def toggle_menu(self):
        self.game_paused = not(self.game_paused)
 
    def title_screen(self):
        self.prev_menu_state = self.menu_state
        if self.menu_state != 'menu' or self.menu_state != 'title' or self.menu_state != 'dead_screen':
            self.toggle_menu()
            self.menu_state = 'menu'
        elif self.menu_state == 'menu' or self.menu_state == 'title' or self.menu_state == 'dead_screen':
            self.toggle_menu()
            self.menu_state  = 'none'

    def run(self):
        self.render()
    
    def init(self):
        self.__init__(self.render)

