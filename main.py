# Rover demo using Simumatik
# author Zion Klinger

from lib.rover import Rover

if __name__ == "__main__":
    rov = Rover()
    while True:
        rov.forward(3,1)
