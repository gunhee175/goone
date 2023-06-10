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

# game setup
WIDTH = 1280
HEIGHT = 720 
VIRTUAL_RES = (800, 600) # CRT shader resolution
REAL_RES = (WIDTH, HEIGHT) # real resolution
FPS = 60 

# set up the colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)


screen = pygame.Surface((800,600)).convert((255, 65280, 16711680, 0))
# 위 코드는 pygame.Surface 클래스를 사용하여 screen 객체를 정의합니다. 
# screen 객체는 게임 창을 나타내는 표면(surface)으로, 너비가 800 픽셀이고 높이가 600 픽셀입니다.
#convert 메서드는 screen 객체에 대해 색상값 튜플을 인자로 받아 호출됩니다. 이 메서드는 원래 표면과 동일한 픽셀 형식을 가지지만 지정된 색상 형식을 가진 새로운 표면을 반환합니다. 이 경우, 색상 형식은 (255, 65280, 16711680, 0)으로 표현되는 32비트 색상 형식입니다. 이 형식은 Pygame에서 투명도를 가진 표면에 일반적으로 사용됩니다.
#색상 형식 튜플은 각각 빨강, 초록, 파랑 및 알파에 대한 색상 값을 나타내는 4-튜플입니다. 각 값은 0에서 255 사이의 정수이며, 0은 최소 강도를 나타내고 255는 최대 강도를 나타냅니다. 알파 값은 표면의 투명도를 나타내며, 0은 완전히 투명하고 255는 완전히 불투명합니다.
#총괄적으로, 이 코드는 800x600 픽셀 크기와 32비트 색상 형식을 가진 screen 객체를 정의합니다. 이 표면은 게임 그래픽을 그리고 화면에 표시하는 데 사용될 수 있습니다.
# screen = pygame.Surface(VIRTUAL_RES).convert((255, 65280, 16711680, 0))



