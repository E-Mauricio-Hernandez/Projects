import paho.mqtt.client as mqtt #import the client1
broker_address="192.168.43.1" 
#broker_address="iot.eclipse.org"
print("creando una nueva instancia")
client = mqtt.Client("P2") #create new instance
print("connectandome al broker")
client.connect(broker_address) #connect to broker
print("Subscribiendome al topico")
client.subscribe("casa/piso1/cuarto1/luz")
print("publicando")
client.publish("casa/piso1/cuarto1/luz","listones")