import os, sys
import pygame

pygame.init()

# for packing game
def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		absolute_path = os.path.join(sys._MEIPASS, relative)
	else:
		absolute_path = os.path.join(relative)
	return absolute_path

screen = pygame.Surface((800,600)).convert((255, 65280, 16711680, 0))


