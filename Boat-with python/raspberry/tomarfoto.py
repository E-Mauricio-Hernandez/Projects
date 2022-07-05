import picamera
from time import sleep

camera = picamera.PiCamera()
while True:
    camera.start_preview()
    sleep(1)
    camera.capture('image_test.jpg', resize=(500,281))
    camera.stop_preview()
    print("listones")
    sleep(5)

camera.close()

