import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
	print(str(message.payload.decode("utf-8")))
	dato=str(message.payload.decode("utf-8"))
	f = open ('datos.txt','w')
	f.write("                                                                                                  ")
	f.close()
	f = open ('datos.txt','w')
	f.write(dato)
	f.close()
    
########################################
broker_address="192.168.43.195"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P25") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic")
client.subscribe("electronica/temp")
#print("Publishing message to topic","house/bulbs/bulb1")
#client.publish("house/bulbs/bulb1","OFF")
time.sleep(90000) # wait
client.loop_forever() #stop the loop
