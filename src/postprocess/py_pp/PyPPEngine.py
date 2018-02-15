"""
Python PostProcess Engine:

Main script to be run to make the postprocess engine operational.
It instantiates a CityManager, starts it, subscribes to the notifications topic
and waits until Ctrl+'C' is pressed.
"""

from CityManager import CityManager
import time


if __name__ == "__main__":

    try:
        TurinManager = CityManager("Turin", 45.106234, 7.619275, 45.024758, 7.719869)
        TurinManager.manage()
        TurinManager.myPyPPEMqttClient.mySubscribe("/city/notifications/#")

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        TurinManager.rest()