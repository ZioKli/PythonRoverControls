from lib.Controller import UDP_Controller
import time

controller = UDP_Controller()
controller.addVariable("sensor", "str", "")
controller.addVariable("left_speed", "float", 0)
controller.addVariable("right_speed", "float", 0)
controller.start()
# All Code Should be written inside these lines
#######################################################################################
# finish this function
# first check to make sure that the parameter speed is greater than 0. If it is less than 0 return
# then set both 'left_speed' and 'right_speed' to be equal to speed.

def forward(speed):
    return

# once you have finished writing the function, run this python script and then start the Simumatik
# if the function is working you should see the rover begin to move
#######################################################################################

if __name__ == '__main__':
    while True:
        forward(3)