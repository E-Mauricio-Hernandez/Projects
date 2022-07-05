import paho.mqtt.client as mqtt 
import time

def on_message(client, userdata, message):
    mensaje=str(message.payload.decode("utf-8"))
    fic = open("info_bote.txt", "a")
    fic.write(mensaje)
    fic.write("\n")
    fic.close()
    print(mensaje)

broker="192.168.1.10"
client = mqtt.Client("kayak3")
print("creando cliente")
client.on_message=on_message 
print("conectandome al broker")
client.connect(broker)
client.loop_start() 
print("subscripcion al topic")
client.subscribe("central/kayak")
while True:
	time.sleep(90000)

client.loop_stop() 