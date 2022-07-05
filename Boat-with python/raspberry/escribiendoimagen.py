import paho.mqtt.client as mqtt
import math
import base64
def convertImageToBase64():
 with open("image_test.jpg", "rb") as image_file:
 encoded = base64.b64encode(image_file.read())
 return encoded

broker_address="192.168.137.1" 
#broker_address="iot.eclipse.org"
print("creando una nueva instancia")
client = mqtt.Client("KAYAK") #create new instance
print("connectandome al broker")
client.connect(broker_address) #connect to broker
print("Subscribiendome al topico")
client.subscribe("central/kayak")



packet_size=3000

def publishEncodedImage(encoded):
 

