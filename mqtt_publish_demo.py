# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish
from random import random
from time import sleep

publish.single("CalgaryKineticEfmLab/test", "Hello", hostname="test.mosquitto.org")
temp = 23

while True:
    temp = temp + (random() - 0.5)*3
    publish.single("CalgaryKineticEfmLab/TempSim", str(temp), hostname="test.mosquitto.org")
    print(temp)
    sleep(60)

print("Done")
 
