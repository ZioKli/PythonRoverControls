# Rover demo using Simumatik
# author Zion Klinger

import time
from rover import Rover

if __name__ == "__main__":
    rov = Rover()
    while True:
        rov.forward(3,1)
