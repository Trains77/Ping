import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

#Script Settings
ball_speed = 5 # speed the ball moves
enable_audio = True # Enable audio
playerspeed = 10 # How fast the player moves

# Gamemodes
bot_player_2 = True # Use a bot for player 2, does not work with Two_balls
bot_player_1 = True # Use a bot for player 1, does not work with Two_balls
increase_ball_speed = False # Increase the ball's speed over time
Two_balls = False # Have 2 balls instead of one, does not work with bot_player_2

# Internal variables
size = [700, 500]
GameName = "Ping"
square_color = (255, 255, 255)
square_size = 15
square_length = 80
game_border1 = size[1] - square_size
game_border2 = 0
game_border3 = size[0] - square_size
fps = 30
player1 = [25,250]
player2 = [655, 250]
game_started = False
ball = [350, 250, "Left", "Up"]
ball2 = [350, 250, "Left", "Up"]
font1 = pygame.font.SysFont('A totally real font', 100)
font2 = pygame.font.SysFont('A totally real font', 40)
move_Down = True
move_Up = True
move_Down1 = True
move_Up1 = True
game_tick = 0
game_tick2 = 0
