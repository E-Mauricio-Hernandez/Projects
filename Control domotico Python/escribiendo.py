import paho.mqtt.client as mqtt #import the client1
broker_address="192.168.43.1" 
#broker_address="iot.eclipse.org"
print("creando una nueva instancia")
client = mqtt.Client("P4") #create new instance
print("connectandome al broker")
client.connect(broker_address) #connect to broker
print("Subscribiendome al topico")
client.subscribe("unillanos/laboratorios/windows/win2")
print("publicando")
mensaje="hola "
client.publish("unillanos/laboratorios/windows/win1",mensaje)
client.publish("unillanos/laboratorios/windows/win2",mensaje)