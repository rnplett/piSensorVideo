from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180
camera.resolution = (720,480)
camera.brightness = 60
camera.capture('data/image.jpg')
