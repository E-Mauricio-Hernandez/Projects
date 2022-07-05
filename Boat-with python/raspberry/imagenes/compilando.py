import serial
import paho.mqtt.client as mqtt
from dronekit import connect
import picamera
from time import sleep
from datetime import datetime

camera = picamera.PiCamera()
vehicle = connect('192.168.137.148:14550', wait_ready=True)
broker_address="192.168.137.1" 
client = mqtt.Client("KAYAK") 
print("connectandome al broker")
client.connect(broker_address) 
print("Listo")
pic=0
camera.start_preview()
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            temperatura = ser.readline().decode('utf-8').rstrip()
            loca=str(vehicle.location.global_frame).split(":")
            camera.start_preview()
            now = str(datetime.now()).split(" ")
            hora=now[1].split(".")
            pic=pic+1
            if pic==100:
                pic=0
            
            nombre=str(pic)+".jpg"
            modo=str(vehicle.mode.name)
            camera.capture(nombre, resize=(500,281))
            datos= str(loca[1]) + " Temp: " + temperatura + " Modo: "+ modo + " " + str(hora[0]) + " F: " +str(pic)
            print(datos)
            client.publish("central/kayak/temperatura",datos)
            camera.stop_preview()
            fic = open("info_bote.txt", "a")
            fic.write(datos)
            fic.write("\n")
            fic.close()
            
camera.close()


