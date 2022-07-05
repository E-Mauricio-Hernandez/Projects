import serial
import paho.mqtt.client as mqtt
from dronekit import connect
import picamera
from time import sleep

camera = picamera.PiCamera()
vehicle = connect('192.168.137.148:14550', wait_ready=True)
broker_address="192.168.137.1" 
client = mqtt.Client("KAYAK") 
print("connectandome al broker")
client.connect(broker_address) 
print("Subscribiendome al topico")
client.subscribe("central/kayak/temperatura")
pic=0
camera.start_preview()
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM2', 9600, timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            temperatura = ser.readline().decode('utf-8').rstrip()
            localizacion= vehicle.location.global_frame
            loca=str(localizacion)
            camera.start_preview()
            sleep(1)
            if(pic==1000):
                pic=0
            else:
                pic=pic+1
            pic1=str(pic)
            nombre="/imagenes/"+pic1+".jpg"
            camera.capture(nombre, resize=(500,281))
            datos= loca + " Temp: " + temperatura + " pic: " + pic1
            client.publish("central/kayak/temperatura",datos)
            camera.stop_preview()
            
camera.close()


