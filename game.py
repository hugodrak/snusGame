import pygame
import random
import time

from pygame.locals import *

tick = 0
pygame.init()
## Initial setup
screen_size = pygame.display.Info()
width, height = int(screen_size.current_w*0.7), int(screen_size.current_h*0.7)
print("W:", width, "H:", height)
#width, height = 640, 480
rate = 5
rot_rate = 10
move_player = False

keys = [False,False,False,False]
playerpos=[100,100]

screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("Fakesnusjakten")

background = pygame.image.load("images/potatisen.jpg")
background = pygame.transform.scale(background, (width, height))

player = pygame.image.load("images/ettan2.png")
enemy = pygame .image.load("images/lyft.png")
enemies = []

margin = 20
rot_rate = 0
rotated_player = player.copy()
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def rand_pos():
    x = int(random.randint(0, width-200))
    y = int(random.randint(0, height-200))
    return (x, y)

start_time = time.time()
while 1:
    tick+=1
    screen.fill(0)
   
    screen.blit(background, (0,0))
    
    rotated_player = rot_center(player, rot_rate)
    
    if len(enemies) == 0 and tick > 100:
        print("win")
        pygame.quit()
        end_time = time.time()
        print("You fininished in:", round(end_time-start_time, 2), "seconds!")
        
        exit(0)

    if len(enemies) >= 3:
        move_player = True
    ## Handle enemy
    if tick % 80 == 0 and len(enemies) < 8:
        pos = rand_pos()
        enemies.append(pos)
    
    for i, enemy_pos in enumerate(enemies):
        screen.blit(enemy, enemy_pos)
        if playerpos[0] < enemy_pos[0]+margin and playerpos[0] > enemy_pos[0]-margin and playerpos[1] < enemy_pos[1]+margin and playerpos[1] > enemy_pos[1]-margin:
            enemies.remove(enemies[i])
             


    screen.blit(rotated_player, playerpos)

    pygame.display.flip()
    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == 'q':
                pygame.quit()
                exit(0)
            if event.key==K_w:
               keys[0]=True
            elif event.key==K_a:
               keys[1]=True
            if event.key==K_s:
               keys[2]=True
            elif event.key==K_d:
               keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==K_w:
               keys[0]=False
            elif event.key==K_a:
               keys[1]=False
            if event.key==K_s:
               keys[2]=False
            elif event.key==K_d:
               keys[3]=False 
    if move_player:
        if keys[0] and keys[1] or keys[2] and keys[3]:
            speed = int(rate*0.75)
        else:
            speed = rate
        if keys[0]:
            playerpos[1]-=speed
        if keys[2]:
            playerpos[1]+=speed
        if keys[1]:
            playerpos[0]-=speed
            rot_rate+=10
        if keys[3]:
            playerpos[0]+=speed
            rot_rate-=10
        

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
