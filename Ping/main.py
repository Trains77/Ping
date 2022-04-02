# Script Modules
import time, sys, colored, os, random, math
from time import sleep
from settings import *
#from colored import fore, back, style

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
pygame.init()

def playsound(channel,audiofile):
    if enable_audio == True:
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound(audiofile))

def image_display(surface, filename, xy):
    img = pygame.image.load(filename)
    surface.blit(img, xy)
def newPlayer(x, y, userID):
    move_down = move_Down
    move_up = move_Up
    move_up1 = move_Up1
    move_down1 = move_Down1
    move_up3 = move_Up3
    move_down3 = move_Down3
    move_down2 = move_Down2
    move_up2 = move_Up2
    if userID == 0:
        if bot_player_1 == False:
            if state[pygame.K_w]:
                if not y <= game_border2:
                    y = y - playerspeed
            if state[pygame.K_s]:
                if not y + square_length - square_size >= game_border1:
                    y = y + playerspeed
        else:
            if ball[1] - y <= 30:
                move_down1 = False
            elif ball[1] - y >= 80:
                move_down1 = True
            if y - ball[1] <= -29:
                move_up1 = False
            elif y - ball[1] <= -9:
                move_up1 = True

            if ball2[1] - y <= 30:
                move_down2 = False
            elif ball2[1] - y >= 80:
                move_down2 = True
            if y - ball2[1] <= -29:
                move_up2 = False
            elif y - ball[1] <= -9:
                move_up2 = True

            if ball[0] <= 325:
                if move_up1 == True:
                    if not y <= game_border2:
                        y -= playerspeed
                elif move_down1 == True:
                    if not y + square_length - square_size >= game_border1:
                        y += playerspeed
            if ball2[0] <= 325:
                if move_up2 == True:
                    if not y <= game_border2:
                        y -= playerspeed
                elif move_down2 == True:
                    if not y + square_length - square_size >= game_border1:
                        y += playerspeed
    elif userID == 1:
        if bot_player_2 == False:
            if state[pygame.K_UP]:
                if not y <= game_border2:
                    y = y - playerspeed
            if state[pygame.K_DOWN]:
                if not y + square_length - square_size >= game_border1:
                    y = y + playerspeed
        else:
            if ball[1] - y <= 30:
                move_down = False
            elif ball[1] - y >= 80:
                move_down = True
            if y - ball[1] <= -29:
                move_up = False
            elif y - ball[1] <= -9:
                move_up = True

            if ball2[1] - y <= 30:
                move_down3 = False
            elif ball2[1] - y >= 80:
                move_down3 = True
            if y - ball2[1] <= -29:
                move_up3 = False
            elif y - ball2[1] <= -9:
                move_up3 = True

            if ball[0] >= 325:
                if move_up == True:
                    if not y <= game_border2:
                        y -= playerspeed
                elif move_down == True:
                    if not y + square_length - square_size >= game_border1:
                        y += playerspeed
            if ball2[0] >= 325:
                if move_up3 == True:
                    if not y <= game_border2:
                        y -= playerspeed
                elif move_down3 == True:
                    if not y + square_length - square_size >= game_border1:
                        y += playerspeed
    return x, y, move_down, move_up, move_down1, move_up1, move_down3, move_up3, move_down2, move_up2
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
            game_tick += 1
            if game_tick == fps:
                game_tick = 0
                game_tick2 += 1
                if game_tick2 >= fps / 4:
                    game_tick2 = 0
                    if increase_ball_speed == True:
                        ballspeed += 1
            # Up Down Movement
            if ball[3] == "Down":
                if ball[1] < game_border1:
                    ball[1] += ballspeed
                else:
                    ball[3] = "Up"
                    ball[1] -= ballspeed
                    playsound(1, "Sounds/hit.wav")
            elif ball[3] == "Up":
                if ball[1] > game_border2:
                    ball[1] -= ballspeed
                else:
                     ball[3] = "Down"
                     ball[1] += ballspeed
                     playsound(1, "Sounds/hit.wav")
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
            if Two_balls == True:
                if ball2[3] == "Down":
                    if ball2[1] < game_border1:
                        ball2[1] += ballspeed
                    else:
                        ball2[3] = "Up"
                        ball2[1] -= ballspeed
                        playsound(1, "Sounds/hit.wav")
                elif ball2[3] == "Up":
                    if ball2[1] > game_border2:
                        ball2[1] -= ballspeed
                    else:
                         ball2[3] = "Down"
                         ball2[1] += ballspeed
                         playsound(1, "Sounds/hit.wav")
                if ball2[2] == "Left":
                    if ball2[0] > game_border2:
                        ball2[0] -= ballspeed
                    else:
                        game_started = False
                else:
                    if ball2[0] < game_border3:
                        ball2[0] += ballspeed
                    else:
                        game_started = False
            player1[0], player1[1], move_Down, move_Up, move_Down1, move_Up1, move_Down3, move_Up3, move_Down2, move_Up2 = newPlayer(player1[0],player1[1],0)
            player2[0], player2[1], move_Down, move_Up, move_Down1, move_Up1, move_Down3, move_Up3, move_Down2, move_Up2 = newPlayer(player2[0],player2[1],1)
        else:
            ballspeed = ball_speed
            left = int(math.ceil(random.randint(1,2)))
            right = int(math.ceil(random.randint(1,2)))
            if left == 1:
                Left = "Left"
                LeftTwo = "Right"
            else:
                Left = "Right"
                LeftTwo = "Left"
            if right == 1:
                Up = "Up"
                UpTwo = "Down"
            else:
                Up = "Down"
                UpTwo = "Up"
            player1 = [25,250]
            player2 = [655, 250]
            ball = [350, 250, Left, Up]
            ball2 = [350, 250, LeftTwo, UpTwo]

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
        if Two_balls == True:
            ball2_square = pygame.draw.rect(screen, square_color, [ball2[0],ball2[1],square_size,square_size])
        else:
            ball2_square = pygame.draw.rect(screen, square_color, [999,999,square_size,square_size])

        if pygame.Rect.colliderect(ball_square, player1_square) == 1:
            ball[2] = "Right"
            playsound(1, "Sounds/hit.wav")
        if pygame.Rect.colliderect(ball_square, player2_square) == 1:
            ball[2] = "Left"
            playsound(1, "Sounds/hit.wav")
        if pygame.Rect.colliderect(ball2_square, player1_square) == 1:
            ball2[2] = "Right"
            playsound(1, "Sounds/hit.wav")
        if pygame.Rect.colliderect(ball2_square, player2_square) == 1:
            ball2[2] = "Left"
            playsound(1, "Sounds/hit.wav")
        pygame.display.flip()
# Quite the execution when clicking on close
pygame.quit()
exit()
