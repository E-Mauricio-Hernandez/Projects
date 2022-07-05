import paho.mqtt.client as mqtt 
import time

def on_message(client, userdata, message):
    temp=str(message.payload.decode("utf-8"))
    print( temp)

broker="192.168.137.1"
client = mqtt.Client("P1")
print("creando cliente")
client.on_message=on_message 
print("conectandome al broker")
client.connect(broker)
client.loop_start() 
print("subscripcion al topic")
client.subscribe("central/kayak/temperatura")
while True:
	time.sleep(90000)
client.loop_stop() 