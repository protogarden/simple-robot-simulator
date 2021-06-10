# example to receiving lidar data from robot
# pygame is required for keyboard events/display
# 
# Tom Van den Bon - 2021/06/10

import time
import pygame
from pygame.locals import *

from math import radians, sin, cos

from core.robot_controller import RobotController

lidarPoints = None

def getTelemetry(message):
    global lidarPoints

    lidarPoints = message['lidar']

rb = RobotController('localhost', 5005, telemetry_callback=getTelemetry)

WIDTH = 500
HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode((500,500)) 
pygame.display.set_caption('Remote Control/Lidar') 
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

    origin = (WIDTH / 2, HEIGHT/2)
    pygame.draw.polygon(screen, (255,255,255), [[origin[0] - 20, origin[1] + 20], [origin[0] + 20, origin[1] + 20], [origin[0], origin[1] - 20] ], 2)

    if lidarPoints != None:
        for point in lidarPoints:
            distance = point['d'] * 40
            angle_degree = point['rx'] 

            (disp_x, disp_y) = (distance * sin(radians(angle_degree)), distance * cos(radians(angle_degree)))
            (end_x, end_y) = (origin[0] + disp_x, origin[1] - disp_y)
          
            pygame.draw.line(screen, (255,255,255), origin, (end_x, end_y))

    clock.tick(60)
    rb.send_cmd_vel(angularVelocity, linearVelocity)
    pygame.display.update()            

pygame.quit()    