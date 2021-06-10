# example of retrieving robot camera for opencv processing
# opencv required
# 
# Tom Van den Bon - 2021/06/10

import time

from core.robot_controller import RobotController
import cv2

campic = None
done = False

def getImage(imageArray):
    global campic 

    temp = imageArray
    campic = cv2.cvtColor(temp, cv2.COLOR_BGR2RGB)

rb = RobotController('localhost', 5005, image_callback=getImage)

while True:
    if campic is not None:
        cv2.imshow("Test", campic)
        cv2.waitKey(1)

