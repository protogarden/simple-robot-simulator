import time

from core.message import IMesgHandler
from core.sim_client import SimClient,SDClient

from io import BytesIO

import base64
import numpy as np
from PIL import Image

class RobotController:
    def __init__(self, host, port, image_callback = None, telemetry_callback = None, odometry_callback = None ):
        self.address = (host, port)
        self.handler = RobotSimHandler(image_callback, telemetry_callback, odometry_callback)
        self.client = SimClient(self.address, self.handler)

    def send_cmd_vel(self, angular_velocity, linear_velocity):
        self.handler.send_cmd_vel(angular_velocity, linear_velocity)

    def send_lidar_config(self, degInc, maxRange):
        self.handler.send_lidar_config(degInc, maxRange)
        

class RobotSimHandler(IMesgHandler):
    def __init__(self, image_callback = None, telemetry_callback = None, odometry_callback = None):
        self.image_callback = image_callback
        self.telemetry_callback = telemetry_callback
        self.odometry_callback = odometry_callback

    def send_lidar_config(self, degInc, maxRange):
        msg = {
            "msg_type" : "lidarconfig",
            "deginc" : degInc.__str__(),
            "maxrange" : maxRange.__str__(),
        }

        self.queue_message(msg)
        time.sleep(0.1)

    def send_cmd_vel(self, angular_velocity, linear_velocity):
        msg = {
            "msg_type" : "cmdvel",
            "av" : angular_velocity.__str__(),
            "lv" : linear_velocity.__str__(),
        }

        self.queue_message(msg)
        time.sleep(0.1)

    def queue_message(self, msg):
        if self.client is None:
            #print(f"skiping: \n {msg}")
            return

        #print(f"sending \n {msg}")
        self.client.queue_message(msg)

    def on_recv_message(self, message):
        #print("Message Received")        

        if message['msg_type'] == 'telemetry':
            #print("Telemetry Received")
            #print(message['image'])
            #print(message['lidar'])

            imgString = message["image"]
            image = Image.open(BytesIO(base64.b64decode(imgString)))
            image_array = np.asarray(image)

            if self.image_callback != None:
                #print("send image")
                self.image_callback(image_array)

            if self.telemetry_callback != None:
                self.telemetry_callback(message)

            #saved_image = Image.fromarray(self.image_array).save('camlive.png')
            return

        if message['msg_type'] == 'robot_odometry':
            if self.odometry_callback != None:
                self.odometry_callback(message)
            return 
            
        print(message)

    def on_connect(self, client):
        print("Socket Connected")
        self.client = client

    def on_disconnect(self):
        print("Socket Disconnected")
        self.client = None

    def on_abort(self, message):
        self.client.stop()