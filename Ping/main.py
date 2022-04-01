# Script Modules
import time, math, sys, colored, os
from time import sleep
from settings import *
#from colored import fore, back, style

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
pygame.init()

def image_display(surface, filename, xy):
    img = pygame.image.load(filename)
    surface.blit(img, xy)
def newPlayer(x, y, userID):
    if userID == 0:
        if state[pygame.K_w]:
            if not y <= game_border2:
                y = y - playerspeed
        if state[pygame.K_s]:
            if not y + square_length - square_size >= game_border1:
                y = y + playerspeed
    elif userID == 1:
        if state[pygame.K_UP]:
            if not y <= game_border2:
                y = y - playerspeed
        if state[pygame.K_DOWN]:
            if not y + square_length - square_size >= game_border1:
                y = y + playerspeed

    return x, y
# Display
screen = pygame.display.set_mode(size)
pygame.display.set_caption(GameName)
done = False
clock = pygame.time.Clock()

while not done:
        clock.tick(fps)

        cursor_pos = pygame.mouse.get_pos()
        mouse_button_list = pygame.mouse.get_pressed(num_buttons=3)
        button_pressed = any(mouse_button_list)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        state = pygame.key.get_pressed()
        if state[pygame.K_ESCAPE]:
            done = True
            print("Quit")

        screen.fill((0, 0, 0))
        if game_started == True:
            # Up Down Movement
            if ball[3] == "Down":
                if ball[1] < game_border1:
                    ball[1] += ballspeed
                else:
                    ball[3] = "Up"
                    ball[1] -= ballspeed
            elif ball[3] == "Up":
                if ball[1] > game_border2:
                    ball[1] -= ballspeed
                else:
                     ball[3] = "Down"
                     ball[1] += ballspeed
            if ball[2] == "Left":
                if ball[0] > game_border2:
                    ball[0] -= ballspeed
                else:
                    game_started = False
            else:
                if ball[0] < game_border3:
                    ball[0] += ballspeed
                else:
                    game_started = False
            player1[0], player1[1] = newPlayer(player1[0],player1[1],0)
            player2[0], player2[1] = newPlayer(player2[0],player2[1],1)
        else:
            player1 = [25,250]
            player2 = [655, 250]
            ball = [350, 250, "Left", "Down"]

            if mouse_button_list[0] == True:
                cursor_square = pygame.draw.rect(screen, (255,0,0), [cursor_pos[0], cursor_pos[1], square_size,square_size])
            else:
                cursor_square = pygame.draw.rect(screen, (255,0,0), [5000, 5000, square_size,square_size])
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, square_color, [75, 75,525,325])
            start_button = pygame.draw.rect(screen, (0,255,0), [285,275,100,50])
            text1 = font1.render("Ping", True, (0,0,0))
            text2 = font2.render("Start", True, (0,0,0))
            screen.blit(text1, (260, 106))
            screen.blit(text2, (300, 285))
            if pygame.Rect.colliderect(cursor_square, start_button) == 1:
                game_started = True
            # screen.blit(text2, (30, 390))

        player1_square = pygame.draw.rect(screen, square_color, [player1[0],player1[1],square_size,square_length])
        player2_square = pygame.draw.rect(screen, square_color, [player2[0],player2[1],square_size,square_length])
        ball_square = pygame.draw.rect(screen, square_color, [ball[0],ball[1],square_size,square_size])

        if pygame.Rect.colliderect(ball_square, player1_square) == 1:
            ball[2] = "Right"
        if pygame.Rect.colliderect(ball_square, player2_square) == 1:
            ball[2] = "Left"
        pygame.display.flip()
# Quite the execution when clicking on close
pygame.quit()
exit()
