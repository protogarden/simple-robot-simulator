import time
import pygame
from pygame.locals import *

from math import radians, sin, cos

from core.robot_controller import RobotController

def getOdometry(message):
    print(message)

rb = RobotController('localhost', 5005, odometry_callback=getOdometry)

WIDTH = 300
HEIGHT = 300

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption('Remote Control/Odometry') 
clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break  

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