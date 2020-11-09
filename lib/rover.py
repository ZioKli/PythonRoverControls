# Author: Zion Klinger
# Description : A class used to control a rover in Simumatik's emulation software. Has all of the functionality to handle initializing a connection with Simumatik's server
import time
from Controller import UDP_Controller
class Rover():
    def __init__(self, slow = 1, medium = 2, fast = 4):
        self.controller = UDP_Controller()
        self.slow = slow
        self.medium = medium
        self.fast = fast
        self.controller.addVariable("sensor", "string", "")
        self.controller.addVariable("left_speed", "float", 0)
        self.controller.addVariable("right_speed", "float", 0)
        self.controller.start()

    def forward(self, speed, duration):
        """
            sends instructions to the Rover to move forward for the specified time
                parameters:
                    speed(float): sets the speed of the robot in radians per second
                    duration(float): sets how long the robot should go forward for
        """
        if speed > 0:
            self.controller.setValue("left_speed", speed)
            self.controller.setValue("right_speed", speed)
            time.sleep(duration)

    def backward(self, speed, duration):
        """
            sends instructions to the Rover to move backward for the specified time
                parameters:
                    speed(float): sets the speed of the robot in radians per second
                    duration(float): sets how long the robot should go backward for
        """
        if speed > 0:
            self.controller.setValue("left_speed", -speed)
            self.controller.setValue("right_speed", -speed)
            time.sleep(duration)

    def right(self, duration):
        """
            sends instructions to the rover to turn right for the specified time
                parameters:
                    duration(float): sets how long the rover should turn for
        """
        self.controller.setValue("left_speed", self.medium)
        self.controller.setValue("right_speed", -self.medium)
        time.sleep(duration)

    def left(self, duration):
        """
            sends instructions to the rover to turn left for the specified time
                parameters:
                    duration(float): sets how long the rover should turn for
        """
        self.controller.setValue("left_speed", -self.medium)
        self.controller.setValue("right_speed", self.medium)
        time.sleep(duration)

    def stop(self, duration):
        """
            sends instructions to the Rover to stop for the specified time
                parameters:
                    duration(float): sets how long the robot should stay stopped for
        """
        self.controller.setValue("left_speed", 0)
        self.controller.setValue("right_speed", 0)
        time.sleep(duration)

    def sensorLeft(self, distance = 1):
        """
            detects any objects on the left within a given distance
                parameters:
                    distance(float) default = 1: the maximum distance to trigger the sensor
                returns:
                    bool: returns true if there is another object within distance
        """
        sensorData = self.controller.getValue("sensor")
        if sensorData != '':
            sensorDataAll = sensorData.split()
            leftData = float(sensorDataAll[7])
            return leftData > -distance

    def sensorRight(self, distance = 1):
        """
            detects any objects on the right within a given distance
                parameters
                    distance(float) default = 1: the maximum distance to trigger the sensor
                returns:
                    bool: returns true if there is another object within distance
        """
        sensorData = self.controller.getValue("sensor")
        if sensorData != '':
            sensorDataAll = sensorData.split()
            rightData = float(sensorDataAll[0])
            return rightData > -distance

    def sensorFront(self, distance = 1):
        """
            detects any objects in front of the rover within a given distance
                parameters
                    distance(float) default = 1: the maximum distance to trigger the sensor
                returns:
                    bool: returns true if there is another object within distance
        """
        sensorData = self.controller.getValue("sensor")
        if sensorData != '':
            sensorDataAll = sensorData.split()
            front3Data = float(sensorDataAll[3])
            front4Data = float(sensorDataAll[4])
            if front3Data > -distance or front4Data > -distance:
                return True
            else:
                return False
