# example to receiving images from robot camera
# pygame is required for keyboard events/display
# 
# Tom Van den Bon - 2021/06/10

import time
import pygame
from pygame.locals import *

import numpy as np
from PIL import Image

from core.robot_controller import RobotController


cameraImage = None

def getImage(imageArray):
    global cameraImage
    temp =  pygame.surfarray.make_surface(imageArray)    
    cameraImage = pygame.transform.flip(pygame.transform.rotate(temp, 270), True, False)


rb = RobotController('localhost', 5005, image_callback=getImage)

pygame.init()
screen = pygame.display.set_mode((1024, 768)) 
pygame.display.set_caption('Remote Control/Camera') 
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
    if cameraImage != None:
        screen.blit(cameraImage, (0,0))


    clock.tick(60)
    rb.send_cmd_vel(angularVelocity, linearVelocity)
    pygame.display.update()            

pygame.quit()    