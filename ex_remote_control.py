# example of sending drive commands to simulator to control robot
# pygame is required for keyboard events
# 
# Tom Van den Bon - 2021/06/10

import time
import pygame
from pygame.locals import *

from core.robot_controller import RobotController

rb = RobotController('localhost', 5005)

pygame.init()
screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption('Remote Control') 
clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_down = pygame.key.get_pressed()

    angularVelocity = 0
    linearVelocity = 0

    if keys_down[K_DOWN]:
        linearVelocity = -1

    if keys_down[K_UP]:
        linearVelocity = 1

    if keys_down[K_LEFT]:
        angularVelocity = -1

    if keys_down[K_RIGHT]:
        angularVelocity = 1

    screen.fill((0,0,0))


    clock.tick(60)
    rb.send_cmd_vel(angularVelocity, linearVelocity)
    pygame.display.update()            

pygame.quit()    
