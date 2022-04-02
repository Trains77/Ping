import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

#Script Settings
bot_player_2 = True # Use AI for player 2
ballspeed = 5 # speed the ball moves
enable_audio = True # Enable audio
playerspeed = 10 # How fast the player moves

# Internal variables
size = [700, 500] # How big the game window should be
GameName = "Ping" # The name of the game
square_color = (255, 255, 255) # The color code of the player square
square_size = 15 # How big should a square be
square_length = 80
game_border1 = size[1] - square_size # The maximum coordinates a player can move
game_border2 = 0 # The minimum coordinates a player can have
game_border3 = size[0] - square_size
fps = 30 # The fps of the game
player1 = [25,250]
player2 = [655, 250]
game_started = False
ball = [350, 250, "Left", "Down"]
font1 = pygame.font.SysFont('A totally real font', 100)
font2 = pygame.font.SysFont('A totally real font', 40)
move_Down = True
move_Up = True
